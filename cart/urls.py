from django.views.generic import RedirectView
from cart import views
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', views.home, name="home"),
	path('items', views.items, name="items"),
	path('gallery', views.gallery, name="gallery"),
	path('user_gallery', views.user_gallery, name="user_gallery"),
	path('user_items', views.user_items, name="user_items"),
	path('settings', views.settings, name="settings"),
	path('login', views.login, name="login"),
]