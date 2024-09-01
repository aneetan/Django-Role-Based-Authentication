from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
#     The choices argument limits the possible values that can be assigned to this field.
# ROLE_CHOICES is expected to be a predefined list or tuple of choices, where each choice is a tuple containing
# two elements: the actual value to be stored in the database and a human-readable name.

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'student'),

    )

    role = models.CharField(max_length=100, choices = ROLE_CHOICES)

