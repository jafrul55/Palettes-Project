from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Color, Palette, Favorite
from .serializers import ColorSerializer, PaletteSerializer, FavoriteSerializer


class PublicPaletteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Palette.objects.filter(is_public=True)
    serializer_class = PaletteSerializer
    permission_classes = [permissions.AllowAny]


class PaletteViewSet(viewsets.ModelViewSet):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def set_visibility(self, request, pk=None):
        palette = self.get_object()
        is_public = request.data.get('is_public')
        palette.is_public = is_public
        palette.save()
        return Response({'message': 'Visibility settings updated.'})


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
