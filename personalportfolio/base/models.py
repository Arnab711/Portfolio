from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    content=models.TextField(max_length=1000)
    number=models.CharField(max_length=10)

    def __self__(self):
        return(self.name)