from django.db import models
from django.utils import timezone
# Create your models here.


class Episode(models.Model):
    name = models.CharField(max_length=150)
    air_date = models.DateField()
    episode = models.CharField(max_length=200)
    url = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=150)
    dimension = models.CharField(max_length=150)
    url = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=200)
    type = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=20)
    origin = models.ForeignKey(Location, related_name="Origin", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="Location", on_delete=models.CASCADE)
    image = models.TextField()
    episode = models.ManyToManyField(Episode, related_name="Episodes")
    url = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
