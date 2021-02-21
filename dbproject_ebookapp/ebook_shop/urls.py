from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
   path("",views.index, name="EbookHome"),
   path("eBooks/",views.eBooks,name='eBooks'),
   path("eBooks/Details/<int:id>",views.Details,name='Details'),
   path('signup/', views.SignUp, name="handleSignUp"),
   path('login/', views.Login, name="handleLogin"),
   path('logout/', views.Logout, name="handleLogout"),
   path('eBooks/Details/<int:id>/download', views.download),
   path('search/',views.search),
   ]
