from django.apps import AppConfig

class ItineraryConfig(AppConfig):
    name = 'it_tracker.itinerary'
    verbose_name="itinerary"

    def ready(self):
        pass
