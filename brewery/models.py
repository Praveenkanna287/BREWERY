from django.db import models

from django.contrib.auth.models import User

class Brewery(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    rating = models.FloatField(default=0)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)