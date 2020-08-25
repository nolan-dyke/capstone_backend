from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.username)

class Flashcard(models.Model):
    traditional = models.CharField(max_length=200)
    simplified = models.CharField(max_length=200)
    pinyin = models.CharField(max_length=200)
    definitions = ArrayField(models.CharField(max_length=200, blank=True), size=8)
    # definitions = models.CharField(max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flashcards')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='flashcards')

    def __str__(self):
        return '%s' % (self.simplified)
