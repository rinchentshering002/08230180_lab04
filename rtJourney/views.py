from django.shortcuts import render
from .models import LearningJourney

# Create your views here.
# View function for home page (index)
# Fetches all learning journey records and displays them
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'journey':journeys})

# View function for "About Me" page
# Displays personal information
def aboutMe(request):
    return render(request, 'aboutMe.html')