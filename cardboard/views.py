from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def home(request):
    
    # project1 = Project()
    # project1.name = "Web Dev"
    # project1.desc = "Web Development Project"
    # project1.img = 'work_3.jpg'
    # project1.price = 1000
    # project1.offer = False
    
    # project2 = Project()
    # project2.name = "Design"
    # project2.desc = "Design Project"
    # project2.img = 'work_4.jpg'
    # project2.price = 500
    # project1.offer = True
    
    # projects = [project1, project2]
    
    projects = Project.objects.all()
    
    
    return render(request, 'index.html', {'projects': projects})