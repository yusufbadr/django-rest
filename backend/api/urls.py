from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home),
    # path('products/', include('products.urls')),
]

