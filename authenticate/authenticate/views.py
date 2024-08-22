from rest_framework.decorators import api_view  #execute views that are invoked via rest api
from rest_framework.response import Response    #generate json responses in response to rest apis


@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    return Response({})

@api_view(['GET'])
def jwtToken(request):
    return Response({})

