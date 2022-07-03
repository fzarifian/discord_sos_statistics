from django.db import models
from django.contrib.auth.models import User
class EventPlanning(models.Model):
    pass

class Game(models.Model):
    name = models.CharField(max_length=32)
    url =  models.CharField(max_length=256, help_text='Define now.gg url for this game', blank=True)

    def __str__(self):
        return self.question_text

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
    event_planning = models.OneToOneField(EventPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return '[%i] %s' % (self.tag, self.name)


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event_planning = models.OneToOneField(EventPlanning, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(default="Add a description for this Event")
    pub_date = models.DateTimeField()
    event_planning = models.OneToOneField(EventPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    pub_date = models.DateTimeField()
    battle_power = models.PositiveBigIntegerField()
    event_planning = models.OneToOneField(EventPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return '[%i] %s' % (self.alliance.name, self.name)

