# -*- coding: uts-8 -*-
from __future__ import absolute_import, unicode_literals

from . import views

from django.conf.urls import url

urlpatterns = [
    #URL pattern for the ItineraryListView
    url(
        regex=r'^(?<username>[\w.@+-]+)/itinerary/$',
        view=views.ItineraryListView.as_view(),
        name='list'
    ),

    #URL pattern for the ItineraryDetailView
    url(
        regex=r'^(?<username>[\w.@+-]+)/itinerary/?<name>[\w.@+-]+/$',
        view=views.ItineraryDetailView.as_view(),
        name='detail'
    ),
]
