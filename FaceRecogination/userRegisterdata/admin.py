from django.contrib import admin
from userRegisterdata.models import UserImage, UserRegister

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_mail', 'user_phone')

admin.site.register(UserRegister, UserAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')

admin.site.register(UserImage, ImageAdmin)


# Register your models here.
