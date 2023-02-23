"""
URLs for greetings.
"""
from django.urls import path  # pylint: disable=unused-import


from .views import GreetingsViewSet

urlpatterns = [
    path('v1/greetings', GreetingsViewSet.as_view(), name='greetings'),
]
