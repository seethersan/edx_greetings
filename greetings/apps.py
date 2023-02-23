"""
greetings Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType


class GreetingsConfig(AppConfig):
    """
    Configuration for the greetings Django application.
    """

    name = 'greetings'
    plugin_app = {
        PluginURLs.CONFIG: {
            # The three dict attributes literally equate to the following
            # lines of code being injected into edx-platform/lms/urls.py:
            #
            # import myapp.urls.py
            # url(r"^my-app/", include((urls, "my_app"), namespace="my_app")),
            #
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^greetings/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        }
    }
