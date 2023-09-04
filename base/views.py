from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets Learn Python!'},
    {'id':2, 'name': 'Frontend developers'},
    {'id':3, 'name': 'Backend developers'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')