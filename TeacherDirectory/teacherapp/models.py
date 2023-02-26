from django.db import models

# Create your models here.

class TeacherDetails(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name  = models.CharField(max_length=100)
    Profile_picture=models.ImageField(upload_to="images_dir")
    Email_Address = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=100)
    Room_Number  = models.CharField(max_length=100)
    Subjects_taught  = models.TextField()
    