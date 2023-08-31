from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'character',CharacterApiView)
router.register(r'episode',EpisodeApiView)
router.register(r'location',LocationApiView)
urlpatterns = router.urls