from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.EmailField()
    password   = models.IntegerField()
    is_staff   = models.BooleanField()
    is_active  = models.BooleanField()
    
    def __str__(self):
        return self.username