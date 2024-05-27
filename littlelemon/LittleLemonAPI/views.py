from django.shortcuts import render
from rest_framework.decorators import api_view
# from .serializers import MenuItemSerializer
from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from .models import MenuItem
# from .models import MenuItems
from .models import Menu
from .models import Booking
from .serializers import MenuSerializer
from .serializers import BookingSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response

# from rest_framework.generics import ListCreateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# from rest_framework import generics, permissions

from rest_framework import generics
from rest_framework import viewsets 
from rest_framework import permissions
from .serializers import *
from .models import *


from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
# from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer



#THIS IS THE LATEST STUFF
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer




# Create your views here. 



#in views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})




# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer


class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated]
   # return Response(serializer.data)


def index(request):
   return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]


# class MenuItemsView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class MenuItemView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

# class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
    


# def post (self, request):
#     serializer = menuSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "success", "data": serializer.data})
    


