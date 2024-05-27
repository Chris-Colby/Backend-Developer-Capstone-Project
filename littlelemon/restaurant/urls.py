from django.contrib import admin
from django.urls import path, include
# from .views import sayHello
from . import views
# from .views import menuview, bookingview



urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    # path('api/', include('restaurant.urls')),
    # path('', sayHello, name='sayHello'), 
    # path('', views.index, name='index'),
    # path('menu/', menuview.as_view()),
    # path('booking/', bookingview.as_view()),
]


# GET THIS GOING - GET THIS CODED IN!!! URL Configuration

# To wire up the API URLs, you can use the DefaultRouter class instead of declaring URL routes in the app and then including it in the project's URLConf.
# router = routers.DefaultRouter()  
# router.register(r'users', views.UserViewSet)  

# urlpatterns = [  

#     path('', include(router.urls)),  
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))  

# The api-auth route is defined to let you use the browsable API feature of DRF.  

