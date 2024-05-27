from django.contrib import admin
from django.urls import path, include
from LittleLemonAPI import views
from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('LittleLemonAPI.urls')),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]


