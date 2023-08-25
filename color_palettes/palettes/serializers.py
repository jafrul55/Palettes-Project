# colorpalettes/serializers.py

from rest_framework import serializers
from .models import Color, Palette, Favorite


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class PaletteSerializer(serializers.ModelSerializer):
    # Use ColorSerializer for dominant_colors
    dominant_colors = ColorSerializer(many=True)
    # Use ColorSerializer for accent_colors
    accent_colors = ColorSerializer(many=True)

    class Meta:
        model = Palette
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
