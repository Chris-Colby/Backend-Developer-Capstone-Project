"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include


# from . import views

from rest_framework.routers import DefaultRouter
from restaurant import views
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
# # from .views import sayHello
# from . import views
# from restaurant import views
# from .views import menuview, bookingview
# from restaurant.views import bookingview
# from restaurant.views import BookingViewSet


 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/menu/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
   # path('', sayHello, name='sayHello'), 
    # # path('', views.index, name='index'),
    # path('menu/', menuview.as_view()),
    # path('booking/', bookingview.as_view()),
    
]
