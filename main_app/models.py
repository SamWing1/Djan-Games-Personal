from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    gamename = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gamename

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
