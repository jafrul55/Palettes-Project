from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Color(models.Model):
    value = models.CharField(max_length=7)

    def __str__(self):
        return self.value


class Palette(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        default=timezone.now)  # Provide a default value
    is_public = models.BooleanField(default=True)

    dominant_colors = models.ManyToManyField(
        Color, related_name='dominant_palettes')
    accent_colors = models.ManyToManyField(
        Color, related_name='accent_palettes')

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
