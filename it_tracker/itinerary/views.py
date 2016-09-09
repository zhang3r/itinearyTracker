# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicod_literals

from .models import Itinerary, City, Hotel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.core.urlresolvers import reverse

class ItineraryDetailView(LoginRequiredMixin, DetailView):
    model = Itinerary
    slug_field='name'
    slug_url_kwarg='name'


class ItineraryUpdateView(LoginRequiredMixin, UpdateView):
    fields =['name', ]

    model = Itinerary

    def get_success_url(self):
        return reverse('itinerary:detail', kwargs={'name':self.request.itinerary.name})

    def get_object(self):
        return Itinerary.objects.get(name=self.request.itinerary.name)


class ItineraryListView(LoginRequiredMixin, ListView):
    model = Itinerary
    slug_field = 'name'
    slug_url_keward = 'name'
