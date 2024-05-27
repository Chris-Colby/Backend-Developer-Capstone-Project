#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers

# from django.db.import models
from .models import Booking, Menu







# from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']








class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'



# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = '__all__'
