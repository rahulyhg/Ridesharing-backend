# Generated by Django 2.1.7 on 2019-03-30 19:15

import django.core.files.storage
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190330_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(max_length=500, storage=django.core.files.storage.FileSystemStorage(location='/home/hasan/Documents/django_project/repository/comingoo/server/mediabrowser_files'), upload_to=user.models.image_upload_path),
        ),
    ]