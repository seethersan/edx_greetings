"""
Database models for greetings.
"""
from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel


class Greetings(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """
    
    message = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return self.message
