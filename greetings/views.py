import logging
import requests


from django.shortcuts import reverse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from openedx.core.lib.api.view_utils import DeveloperErrorViewMixin, view_auth_classes


from .serializers import GreetingsSerializer
from .models import Greetings


LOGGER = logging.getLogger(__name__)


@view_auth_classes(is_authenticated=True)
class GreetingsViewSet(DeveloperErrorViewMixin, ModelViewSet):
    """
    A viewset for viewing and editing greetings.
    """
    serializer_class = GreetingsSerializer
    queryset = Greetings.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Create a new Greetings instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        LOGGER.info(serializer.data["message"])        
        serializer.save()
        if serializer.data["message"] == "Hello":
            url = reverse('greetings')
            user = request.user
            response = requests.post(url, data = {'message': 'goodbye'})
        return Response(serializer.data, status=status.HTTP_201_CREATED)