from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.

def home(request, self):
    # context=RequestContext(request)
    return HttpResponse('Worked')

