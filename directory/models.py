from django.db import models
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class Teachers(models.Model):

    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    profileimg = models.ImageField(upload_to='profile')
    email = models.EmailField(blank=True,unique=True)
    phone = models.CharField(max_length=150)
    room_number = models.CharField(max_length=50)
    subjects = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
# Create your models here.
