from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=32, help_text='Define a name for this game')
    url =  models.CharField(max_length=256, help_text='Define now.gg url for this game', blank=True)

    def __str__(self):
        return self.name

class Instance(models.Model):
    name = models.CharField(max_length=32)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Alliance(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=3)
    description = models.TextField(default="Add a description for this Alliance")
    pub_date = models.DateTimeField()
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

    def __str__(self):
        return '[%s] %s' % (self.tag, self.name)

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(default="Add a description for this Event")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    pub_date = models.DateTimeField()
    battle_power = models.PositiveBigIntegerField()

    def __str__(self):
        return '[%i] %s' % (self.alliance.name, self.name)

class EventPlanning(models.Model):
    alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    begin_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
