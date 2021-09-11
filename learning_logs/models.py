from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """ A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self) -> str:
        """return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """ user can enter their journal"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."
