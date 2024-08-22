from rest_framework.decorators import api_view  #execute views that are invoked via rest api
from rest_framework.response import Response    #generate json responses in response to rest apis

from .serializers import UserSerializer        # write json objects on database
from rest_framework import status               #return status code 201 or 400
from rest_framework.authtoken.models import Token  
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes  
from rest_framework.authentication import SessionAuthentication, TokenAuthentication #authenticate session with tokens
from rest_framework.permissions import IsAuthenticated #declare that API only works if the user is authenticated 


@api_view(['POST'])
def login(request):
    #return 404 if user is not found 
    user = get_object_or_404(User, username = request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    

    token = Token.objects.get(user = user)
    serializer = UserSerializer(instance = user )
    return Response({"token": token.key, "user": serializer.data})


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
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def jwtToken(request):
    return Response("passed for {}".format(request.user.email))

