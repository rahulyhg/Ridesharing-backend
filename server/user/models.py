from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .appconfig import MB_STORAGE
from django.urls import reverse

# Create your models here.
def image_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/images/{1}'.format(instance.user.id, filename)


def file_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/files/{1}'.format(instance.user.id, filename)

class Bank(models.Model):
    bank_name = models.CharField(max_length=150)

    def __str__(self):
        return self.bank_name

class UserProfile(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    phone  = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    user_image = models.ImageField(upload_to=image_upload_path, max_length=500, storage=MB_STORAGE)

    city = models.CharField(max_length=50)
    bank_account_no = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, related_name='user_profile', on_delete=models.CASCADE)
    user_id_number = models.CharField(max_length=100)
    id_photo_upper = models.ImageField(_("Id Card Upper Image"),upload_to=file_upload_path, max_length=500, storage=MB_STORAGE)
    id_photo_bottom = models.ImageField(_("Id Card Bottom Image"),upload_to=file_upload_path, max_length=500, storage=MB_STORAGE)
    driving_license_number = models.CharField(max_length=100)
    driving_license_photo_upper =  models.ImageField(_("Driving License Upper Image"),upload_to=file_upload_path, max_length=500, storage=MB_STORAGE)

    driving_license_photo_bottom = models.ImageField(_("Driving License Bottom Image"),upload_to=file_upload_path,max_length=500, storage=MB_STORAGE)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.user.username