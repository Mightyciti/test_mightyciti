# Generated by Django 4.0.4 on 2022-05-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Church_Name', models.CharField(max_length=100, null=True)),
                ('Presents', models.CharField(max_length=50, null=True)),
                ('Theme', models.CharField(max_length=800, null=True)),
                ('Date', models.CharField(max_length=70, null=True)),
                ('Time', models.CharField(max_length=70, null=True)),
                ('Venue', models.CharField(max_length=150, null=True)),
                ('Enquiry_Lines', models.CharField(max_length=100, null=True)),
                ('Ministering', models.CharField(max_length=200, null=True)),
                ('Program_Design', models.ImageField(blank=True, null=True, upload_to='task_upload')),
            ],
        ),
    ]