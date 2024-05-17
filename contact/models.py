from django.db import models

# Create your models here.
class Contactmodel(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
