#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
