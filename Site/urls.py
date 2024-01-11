from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('research/', views.research, name='research'),
    path('docs/', views.docs, name='docs'),
    path('giaotrinh/',views.giaotrinh, name='giaotrinh'),
    path('lecturer/', views.lecturer, name='lecturer'),
    
]