#from django.shortcuts import render
#from django.contrib.auth.models import User
#from django.shortcuts import get_object_or_404
#from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        return Response({'OIIIIIIII'});

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
