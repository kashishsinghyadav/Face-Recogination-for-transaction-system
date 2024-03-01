import os
import base64
import face_recognition 
from django.conf import settings
from django.http import JsonResponse

def face_recognition_view(request):
    if request.method == 'POST':
        try:
            image_data = request.POST.get("current_image")
            email = request.POST.get("email")

            # Decode base64 image data
            header, encoded = image_data.split(",", 1)
            data = base64.b64decode(encoded)
            
            # Define the file path to save the image
            image_path = os.path.join(settings.MEDIA_ROOT, "image", "media", "image.png")

            # Write the image data to the file
            with open(image_path, "wb") as f:
                f.write(data)

            # Load submitted image and existing image
            got_image = face_recognition.load_image_file('/media/images')
            existing_image = face_recognition.load_image_file(os.path.join(settings.MEDIA_ROOT, "image", "students", f"{email}.jpg"))

            # Extract facial features
            got_image_facialfeatures = face_recognition.face_encodings(got_image)[0]
            existing_image_facialfeatures = face_recognition.face_encodings(existing_image)[0]

            # Compare facial features
            results = face_recognition.compare_faces([existing_image_facialfeatures], got_image_facialfeatures)

            # Return JSON response based on the result
            if results[0]:
                return JsonResponse({'message': f'Welcome {email}'})
            else:
                return JsonResponse({'message': 'Face not recognized'})
        except Exception as e:
            # Handle any exceptions
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
