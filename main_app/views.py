from django.shortcuts import render
#from .models import Finch

class Finch: 
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

finches = [
  Finch('Doug', 'zebra', 'friendly', 7),
  Finch('Max', 'american', 'rude and loud', 5),
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})