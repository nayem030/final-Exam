from django.db import models
from accounts.models import Account

class Item(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField()
    image =  models.ImageField(upload_to='photos/post')
    
    def __str__(self):
        return self.title
