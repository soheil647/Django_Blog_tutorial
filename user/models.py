from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(*args, **kwargs).save()

        image = Image.open(self.img.path)
        if image.width > 300 or image.height > 300:
            image.thumbnail((300,300))
            image.save(self.img.path)
