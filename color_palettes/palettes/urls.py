# colorpalettes/urls.py

from rest_framework.routers import DefaultRouter
from .views import PublicPaletteViewSet, PaletteViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'public-palettes', PublicPaletteViewSet, basename='public-palettes')
router.register(r'palettes', PaletteViewSet)
router.register(r'favorites', FavoriteViewSet, basename='favorites')  # Use the correct viewset name

urlpatterns = router.urls
