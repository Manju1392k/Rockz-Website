from distutils.command.upload import upload
from django.db import models

# Create your models here.
class RocketBlog(models.Model):
    Rocket_Name = models.CharField(max_length=150)
    Rocket_LaunchDate = models.CharField(max_length=10)
    Rocket_LandingDate = models.CharField(max_length=10)
    Rocket_Image = models.ImageField(upload_to ='photos')
    Rocket_Time = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.Rocket_Name