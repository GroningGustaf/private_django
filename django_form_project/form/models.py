from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    age = models.IntegerField(
        validators=[
            MaxValueValidator(115),
            MinValueValidator(16)
        ]
    )
    times_logged_in = models.IntegerField(default=0) # ska gå upp 1 varje gång man loggar in, bara för att testa skicka data fram och tillbaka
    

