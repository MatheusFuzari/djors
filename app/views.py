from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
class CharacterApiView(ModelViewSet):
  queryset = Character.objects.all()
  serializer_class = CharactersSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['name','gender']
  permission_classes = (IsAuthenticated,)
class LocationApiView(ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields= ['dimension']
class EpisodeApiView(ModelViewSet):
  queryset = Episode.objects.all()
  serializer_class = EpisodeSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['air_date','episode']

'''
class LocationApiView(APIView):
  def post(self,request):
    locationJson = request.data
    LocationSerialized = LocationSerializer(data=locationJson)
    LocationSerialized.is_valid(raise_exception=True)
    LocationSerialized.save()
    return Response(data=LocationSerialized.data, status=status.HTTP_201_CREATED)
  def get(self,request,id=''):
    if(id==''):
      if('type' in request.GET):
        location_found = Location.objects.filter(type=request.GET['type'])
        locationSerialized = LocationSerializer(location_found, many=True)
        return Response(locationSerialized.data)
      location_found = Location.objects.all()
      locationSerialized = LocationSerializer(location_found, many=True)
      return Response(locationSerialized.data)
    try:
      location_found = Location.objects.get(id=id)
      locationSerialized = LocationSerializer(location_found, many=False)
      return Response(locationSerialized.data)
    except Location.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND, data="Location not found!")
  def delete(self,request,id=''):
    if(id == ''):
      return Response(data="No id given", status=status.HTTP_400_BAD_REQUEST)  
    else:
      try:
        location_found = Location.objects.get(id=id)
        location_found.delete()
        return Response(data="Deleted!", status=status.HTTP_204_NO_CONTENT)  
      except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data="Location not found!")
  def patch(self,request,id=''):
    if(id==''):
      return Response(status=status.HTTP_400_BAD_REQUEST, data='No id given')
    else:
      try:
        locationJson = request.data
        location_found = Location.objects.get(id=id)
        locationSerialized = LocationSerializer(location_found,data=locationJson,partial=True)
        locationSerialized.save()
        return Response(data=locationSerialized.data, status=status.HTTP_200_OK)
      except Location.DoesNotExist:
        return Response(data='Location not found', status=status.HTTP_404_NOT_FOUND)
  def put(self,request,id=''):
    if(id==''):
      return Response(status=status.HTTP_400_BAD_REQUEST, data='No id given')
    else:
      try:
        locationJson = request.data
        location_found = Location.objects.get(id=id)
        locationSerialized = LocationSerializer(location_found,data=locationJson)
        locationSerialized.save()
        return Response(data=locationSerialized.data, status=status.HTTP_200_OK)
      except Location.DoesNotExist:
        return Response(data='Location not found', status=status.HTTP_404_NOT_FOUND)
        
class EpisodeApiView(APIView):
  def post(self,request):
    episodeJson = request.data
    episodeSerialized = EpisodeSerializer(data=episodeJson)
    episodeSerialized.is_valid(raise_exception=True)
    episodeSerialized.save()
    return Response(data=episodeSerialized.data,status=status.HTTP_201_CREATED)
  def get(self,request,id=''):
    if(id==''):
      episode_found = Episode.objects.all()
      episodeSerialized = EpisodeSerializer(episode_found, many=True)
      return Response(episodeSerialized.data)
    try:
      episode_found = Episode.objects.get(id=id)
      episodeSerialized = EpisodeSerializer(episode_found, many=False)
      return Response(episodeSerialized.data)
    except Episode.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND, data='Episode not found!')
  def delete(self,request,id=''):
    if(id == ''):
      return Response(status=status.HTTP_400_BAD_REQUEST, data='Id not given!')
    else:
      try:
        episode_found = Episode.objects.get(id=id)
        episode_found.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data='Deleted!')
      except Episode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data="Episode not found!")
  def patch(self, request, id=''):
    if(id==""):
      return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
      try:
        episodeJson = request.data
        episode_found = Episode.objects.get(id=id)
        episodeSerialized = EpisodeSerializer(episode_found,data=episodeJson,partial=True)
        episodeSerialized.is_valid(raise_exception=True)
        episodeSerialized.save()
        return Response(data=episodeSerialized.data, status=status.HTTP_200_OK)
      except Episode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Episode not found!')
  def put(self, request, id=''):
    if(id==""):
      return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
      try:
        episodeJson = request.data
        episode_found = Episode.objects.get(id=id)
        episodeSerialized = EpisodeSerializer(episode_found,data=episodeJson)
        episodeSerialized.is_valid(raise_exception=True)
        episodeSerialized.save()
        return Response(data=episodeSerialized.data, status=status.HTTP_200_OK)
      except Episode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Episode not found!')

class CharacterApiView(APIView):
  def post(self,request):
    characterJson = request.data
    characterSerialized = CharactersSerializer(data=characterJson)
    characterSerialized.is_valid(raise_exception=True)
    characterSerialized.save()
    return Response(data=characterSerialized.data, status=status.HTTP_201_CREATED)
  def get(self,request,id='',base=''):
      // send by url (u've used php, doesnt miss)
      //if 'heigh' in request.GET:
      //  character_found = Character.objects.filter(height__gt=request.GET['height])
      //  characterSerialized = CharactersSerializer(character_found, many=True)
      //  return Response(peopleSerialized.data)
    if(id=='' and base ==''):
      character_found = Character.objects.all()
      characterSerialized = CharactersSerializer(character_found, many=True)
      return Response(characterSerialized.data)
    elif(id !='' and base==''):
      try:
        character_found = Character.objects.get(id=id)
        characterSerialized = CharactersSerializer(character_found, many=False)
        return Response(characterSerialized.data)
      except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Character not found!')
    elif(id!='' and base!=''):
        teste = []
        start = 0
        stop = base
        while(start != stop):
          try:
            character_found = Character.objects.get(id=(id+start))
            characterSerialized = CharactersSerializer(character_found, many=False)
            teste.append(characterSerialized.data)
            start+=1
          except Character.DoesNotExist:
            start+=1
            stop+=1
            if(base>Character.objects.all().count()):
              return Response(status=status.HTTP_400_BAD_REQUEST, data="Id not found!")
        return Response(teste)
  def delete(self,request,id=''):
    if(id==''):
      return Response(status=status.HTTP_400_BAD_REQUEST, data='Id not given!')
    else:
      try:
        character_found = Character.objects.get(id=id)
        character_found.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data='Deleted!')
      except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Character not found!')
  def patch(self,request,id=''):
    if(id==''):
      return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
      try:
        characterJson = request.data
        character_found = Character.objects.get(id=id)
        characterSerialized = CharactersSerializer(character_found, data=characterJson, partial=True)
        characterSerialized.is_valid(raise_exception=True)
        characterSerialized.save()
        return Response(data=characterSerialized.data, status=status.HTTP_200_OK)
      except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Character not found!')
  def put(self,request,id=''):
    if(id==''):
      return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
      try:
        characterJson = request.data
        character_found = Character.objects.get(id=id)
        characterSerialized = CharactersSerializer(character_found, data=characterJson)
        characterSerialized.is_valid(raise_exception=True)
        characterSerialized.save()
        return Response(data=characterSerialized.data, status=status.HTTP_200_OK)
      except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Character not found!')
'''