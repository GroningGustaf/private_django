from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import user
def index(request):
    return HttpResponse("hello world, your at the form-apps index")

def userSearch(request):
    response = "you're looking for the user at id %s"
    all_entries = user.objects.all()
    return HttpResponse(all_entries)

