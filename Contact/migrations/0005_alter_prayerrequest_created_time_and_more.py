# Generated by Django 4.0.4 on 2022-05-06 23:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0004_prayerrequest_created_time_testimony_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayerrequest',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 0, 40, 13, 595823)),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 0, 40, 13, 594824)),
        ),
    ]
