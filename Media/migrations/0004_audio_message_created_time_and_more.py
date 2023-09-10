# Generated by Django 4.0.4 on 2022-05-06 23:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0003_remove_photo_gallery_image_file_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_message',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 0, 38, 58, 643142)),
        ),
        migrations.AddField(
            model_name='photo_gallery',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 0, 38, 58, 643142)),
        ),
        migrations.AddField(
            model_name='video_message',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 0, 38, 58, 643142)),
        ),
    ]