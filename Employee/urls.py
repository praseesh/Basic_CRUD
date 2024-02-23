from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('addemployee/', views.addemployee, name='addemployee'),
]
