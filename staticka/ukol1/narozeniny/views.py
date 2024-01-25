from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "narozeniny/index.html")

def form(request):
    return render(request, "narozeniny/form.html")

 

