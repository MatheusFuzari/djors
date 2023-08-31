from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Episode)
class detEpisode(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ['id','name']
    
@admin.register(Location)
class detLocation(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ['id','name']

@admin.register(Character)
class detCharacter(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ['id','name']