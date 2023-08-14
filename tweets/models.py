from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    image = models.ImageField(blank=True, upload_to='post_pictures')
    created = models.DateField(auto_now_add=True)