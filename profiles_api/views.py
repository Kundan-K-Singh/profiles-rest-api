#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.

class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        "Uses HTTP mathods as functions(get, put, post, patch, delete)",
        "Is similar to Django View",
        "Gives most ctrl over logic",
        "Is mapped manually to URLs",
        ]
        return Response({'message': 'Hello there!', 'an_apiview' : an_apiview})

    def post(self, request):
        """Creates a hello post with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})

    def patch(self, response, pk= None):
        """ HAndles partial update of the object"""
        return Response({'method' : "POST"})

    def delete(self, request, pk = None):
        """Handles deleting of object"""
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
        'Uses actions (list, retrieve, create, update, partial update)',
        'Automaticlly maps to usrls using router',
        'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello message!"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!'
            return Response({'message' : message, 'method': 'crearte from Viewset'})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk = None):
        """Handles getting an object by its id"""
        return Response({'http_method' : 'GET'})

    def update(self, request, pk = None):
        """handle updating a request"""
        return Response({'http_method' : 'UPDATE'})

    def partial_update(self, request, pk = None):
        """handle Partially updating a request"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk = None):
        """handle deleting a request"""
        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
