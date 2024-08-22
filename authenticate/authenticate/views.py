from rest_framework.decorators import api_view  #execute views that are invoked via rest api
from rest_framework.response import Response    #generate json responses in response to rest apis

from .serializers import UserSerializer        # write json objects on database
from rest_framework import status               #return status code 201 or 400
from rest_framework.authtoken.models import Token  #fetch and create user and token
from django.contrib.auth.models import User


@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        new_user = User.objects.get(username = request.data['username'])

        #to ensure hashed pw
        new_user.set_password(request.data['password'])
        new_user.save()

        token = Token.objects.create(user = new_user)

        return Response({"token": token.key,
                         "user": serializer.data})
     
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def jwtToken(request):
    return Response({})

