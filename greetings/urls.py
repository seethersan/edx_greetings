"""
URLs for greetings.
"""
from django.urls import path  # pylint: disable=unused-import


from .views import GreetingsViewSet

urlpatterns = [
    path('', GreetingsViewSet.as_view(), name='greetings'),
]
