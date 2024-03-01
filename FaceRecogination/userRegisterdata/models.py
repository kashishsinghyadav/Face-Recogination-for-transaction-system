from django.db import models

class UserRegister(models.Model):
    user_name = models.CharField(max_length=50)
    user_mail = models.EmailField()
    user_phone = models.CharField(max_length=12)
    
    def __str__(self):
         
        return self.user_mail
    
class UserImage(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')



# Create your models here.
