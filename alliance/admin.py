from django.contrib import admin
from .models import Game, Instance, Alliance, Event, Player

# Register your models here.


class PlayerInline(admin.StackedInline):
    model = Player
    extra = 3

class InstanceInline(admin.StackedInline):
    model = Instance
    extra = 3

class EventInline(admin.StackedInline):
    model = Event
    extra = 3

class AllianceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['instance', 'name', 'tag']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [PlayerInline]

class GameAdmin(admin.ModelAdmin):
    inlines = [InstanceInline]

admin.site.register(Alliance, AllianceAdmin)
admin.site.register(Game, GameAdmin)

