# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ..users.models import User

@python_2_unicode_compatible
class Itinerary(models.Model):
    name = models.CharField('Name of Trip', blank=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('itinerary:detail', kwargs={'name':self.name})

@python_2_unicode_compatible
class city(models.Model):
    name = models.CharField('Name of City', blank=True, max_length=255)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    #TODO zzz implement more fields
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name
    class Meta:
        ordering=['start_date',]

@python_2_unicode_compatible
class hotel(models.Model):
    name = models.CharField('Hotel Name', blank=True, max_length=255)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
