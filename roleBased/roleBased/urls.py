 
from django.contrib import admin
from django.urls import path, include
from authentication.views import UserRegistration, UserLoginView, UserLogoutView

urlpatterns = [
    path('api/register/', UserRegistration.as_view(), name="user-registration"),
    path('api/login/', UserLoginView.as_view(), name="user-login"),
    path('api/logout/', UserLogoutView.as_view(), name="user-logout"),

]
