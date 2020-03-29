from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
	return render(request, 'login.html')
	
def home(request):
	return render(request, 'home.html')

def items(request):
	return render(request, 'items.html')
	
def gallery(request):
	return render(request, 'gallery.html')
	
def user_items(request):
	return render(request, 'user_items.html')
	
def user_gallery(request):
	return render(request, 'user_gallery.html')
	
def settings(request):
	return render(request, 'settings.html')