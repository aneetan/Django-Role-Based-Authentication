from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializers):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']