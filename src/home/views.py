from platform import system
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html", {
        "data": ["body_message","Scaune project"]
    })
