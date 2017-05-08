from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from myvaletapp.models import ParkingLot
def home(request):
    return render(request, "home.html",{})

def initMap(request):
	if request.method == "POST":
	{
		
	}
    return render(request, "mapDraft.html",{})
    
