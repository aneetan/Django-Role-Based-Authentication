from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    #metadata for serializer
    class Meta:
        model = User
        fields = ['username', 'email', 'role','password']
        #setting write only True in password to prevent it from being exposed in responses
        extra_kwargs = {'password':{'write_only': True}}

        # when a new user is created via the serializer. It receives validated_data
        def create(self, validated_data):
            #create a new user instance
            #(**validated_data) syntax unpacks the dictionary and passes the keys and values as keyword arguments
            user = User.objects.create_user(**validated_data)
            return user