from django.db import models

class Profile(models.Model):
    username   = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    avatar     = models.FileField(upload_to='media/images',max_length=255,null=True)
    email      = models.EmailField(max_length=100)
    password   = models.CharField(max_length=32)
    is_staff   = models.BooleanField()
    is_active  = models.BooleanField()
    
    def __str__(self):
        return self.username
    