"""
Admin registration for Greetings.
"""

from django.contrib import admin

from .models import Greetings

admin.site.register(Greetings)