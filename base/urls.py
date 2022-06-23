from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.home, name='home'),
    path('login/',views.LoginInterfaceView.as_view(),name='login'),
    path('register/',views.SignupView.as_view(),name='register'),
    path('logout/', views.logoutUser, name='logout'),

]