from django.shortcuts import render
from .models import Rooms
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Home page view 
@login_required
def home_page(request):
    return render(request, 'home_page/home_page.html')

# To view the different rooms available 
@login_required
def detail(request):
    rooms = Rooms.objects.all()
    return render(request, 'home_page/detail.html', {"rooms": rooms})

# To view contact information
@login_required 
def contact(request):
    return render(request, 'home_page/contact.html')

# To get information about each room 

class RoomView(LoginRequiredMixin, DetailView):
    model = Rooms
