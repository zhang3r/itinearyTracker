# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .models import Itinerary, City, Hotel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView
from django.core.urlresolvers import reverse
from ..users.models import User
class ItineraryDetailView(LoginRequiredMixin, DetailView):
    model = Itinerary
    slug_field='name'
    slug_url_kwarg='name'
    def get_object(self):
        return Itinerary.objects.get(username=self.request.itinerary.username)

class ItineraryUpdateView(LoginRequiredMixin, UpdateView):
    fields =['name', ]

    model = Itinerary

    def get_success_url(self):
        return reverse('itinerary:list')
    def get_object(self):
        return Itinerary.objects.get(user=User.objects.get(username=self.request.user.username))
       


class ItineraryListView(LoginRequiredMixin, ListView):
    model = Itinerary
    slug_field = 'username'
    slug_url_keward = 'username'
    def get_object(self, **kwargs):
        return User.objects.get(username=kwargs['username'])

class ItineraryCreateView(LoginRequiredMixin, CreateView):
    model=Itinerary
    fields=['name',]
    def get_success_url(self):
        return reverse('itinerary:list')

    def get_object(self):
        return User.objects.get(username=kwargs['username'])
