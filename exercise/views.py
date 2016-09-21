from django.shortcuts import render

from .models import  Pullup

# Create your views here.

def index(request):
    pullups = Pullup.objects.all()

    context = {
        "pullups": pullups
    }
    
    return render(request, "exercise/index.html", context)
