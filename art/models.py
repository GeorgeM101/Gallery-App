from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 20)

    def __str__ (self):
        return self.name

class Image(models.Model):
    picture = models.CharField('image')
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.picture
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_category(cls,search_term):
        image = cls.objets.filter()