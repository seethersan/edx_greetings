"""
URLs for greetings.
"""
from django.urls import path  # pylint: disable=unused-import
from rest_framework.routers import DefaultRouter


from .views import GreetingsViewSet

router = DefaultRouter()
router.register(r'', GreetingsViewSet, basename='greetings')
urlpatterns = router.urls
