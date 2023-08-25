# ColorPalettesProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the app's URL configuration
    path('', include('palettes.urls')),
    path('account/', include('user_app.urls')),
]
