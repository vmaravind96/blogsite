from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    def save(self):
        super().save()
        image = Image.open(self.image.path).convert('RGB')
        if image.height > 150 or image.width > 150:
            size = (150, 150)
            image.thumbnail(size)
            image.save(self.image.path)
