from django.db import models

# Create your models here.

class Books(models.Model):
    name=models.CharField(unique=True,max_length=200)
    price=models.PositiveIntegerField(max_length=200)
    author=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True,upload_to="images")

    def __str__(self):
        return self.name
