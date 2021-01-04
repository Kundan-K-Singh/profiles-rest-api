#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test APIView"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        "Uses HTTP mathods as functions(get, put, post, patch, delete)",
        "Is similar to Django View",
        "Gives most ctrl over logic",
        "Is mapped manually to URLs",
        ]
        return Response({'message': 'Hello there!', 'an_apiview' : an_apiview})
