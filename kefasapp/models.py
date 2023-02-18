from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Video(models.Model):
    video1 = CloudinaryField(resource_type='video',)