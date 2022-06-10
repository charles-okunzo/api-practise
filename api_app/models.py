from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    lavel = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.name