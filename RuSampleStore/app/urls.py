"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from store.views import main_page, PackViewSet, SampleViewSet, LabelViewSet, RelationView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'label', LabelViewSet)
router.register(r'pack', PackViewSet, basename='pack')
router.register(r'sample', SampleViewSet, basename='sample')
router.register(r'relation', RelationView)

urlpatterns = [
                  path('', main_page),
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('api/auth/', include('djoser.urls')),
                  path('api/auth/', include('djoser.urls.authtoken')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
