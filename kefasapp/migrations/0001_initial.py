# Generated by Django 4.1.7 on 2023-02-18 09:56

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video1', cloudinary.models.CloudinaryField(max_length=255)),
            ],
        ),
    ]
