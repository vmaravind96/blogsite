from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user.username)