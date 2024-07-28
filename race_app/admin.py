from django.contrib import admin
from .models import Race, Horse

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('date', 'location')
    list_filter = ('date', 'location')
    search_fields = ('location',)

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'weight', 'odds', 'popularity', 'race', 'jockey', 'trainer', 'body_weight', 'body_weight_change')
    list_filter = ('race', 'jockey', 'trainer')
    search_fields = ('name', 'jockey', 'trainer')
    list_editable = ('weight', 'odds', 'popularity', 'body_weight', 'body_weight_change')

