from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "index.html", {})

###
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
    # path('course/', views.course, name='course'),
    # path('research/', views.research, name='research'),
    # path('docs/', views.docs, name='docs'),
    # path('giaotrinh/',views.giaotrinh, name='giaotrinh'),
    # path('lecturer/', views.lecturer, name='lecturer'),
    
###

def contact(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})

def course(request):
    return render(request, "course.html", {})

def docs(request):
    return render(request, "docs.html", {})

def giaotrinh(request):
    return render(request, "giaotrinh.html", {})

def lecturer(request):
    return render(request, "lecturer.html", {})

def research(request):
    return render(request, "research.html", {})