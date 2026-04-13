from django.urls import path
from jobapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hyderabad/', views.hyderabad, name='hyderabad'),
    path('chennai/', views.chennai, name='chennai'),
    path('bangalore/', views.bangalore, name='bangalore'),
    path('pune/', views.pune, name='pune'),
]