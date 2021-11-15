from django.db import models
from django.urls import reverse

class Post(models.Model):
    username = models.CharField(max_length=50)
    img_url = models.CharField(max_length=10000)
    description = models.TextField()

    def __str__(self):
        return self.username + " | " + "Post"

    def get_absolute_url(self):
        return reverse('home')
