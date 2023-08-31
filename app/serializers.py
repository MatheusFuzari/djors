from rest_framework import routers, serializers, views
from .models import *
class EpisodeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Episode
    fields = '__all__'
    many = True
    
class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'
    many = True

class CharactersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Character
    fields = '__all__'
    many = True