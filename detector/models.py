from django.db import models

# Create your models here.
# Create your models here.
class images(models.Model):
    image_name = models.CharField(max_length=100)
    image_url = models.FileField(upload_to='Images/')

class detected(models.Model):
    image_name = models.CharField(max_length=100)
    image_url = models.FileField(upload_to='Images/')