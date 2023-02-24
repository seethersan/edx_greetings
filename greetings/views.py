import logging
import requests


from django.urls import reverse
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
        serializer.save()
        LOGGER.info(serializer.validated_data["message"])
        if serializer.validated_data["message"] == "hello":
            url = request.build_absolute_uri(reverse('greetings:greetings-list'))
            response = requests.post(url, data = {'message': 'goodbye'}, headers={"Authorization": f"Bearer {str(request.auth)}"})
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_201_CREATED)