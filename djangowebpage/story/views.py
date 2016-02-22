from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Line

def home(request):
	#return HttpResponse("Hello world!")
	return render_to_response("story/home.html", {'lines': Line.object.all()})
	# when you want to make a response from a template then you make a dict
