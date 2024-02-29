from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('display/', views.display, name = "display"),
    path('del/', views.delete, name='delete'),
    path('update/', views.update, name='update'),

]
