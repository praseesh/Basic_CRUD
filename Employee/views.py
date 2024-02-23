from django.shortcuts import render
from .models import Employee

def home(request):
    return render(request, "index.html")

def addemployee(request):
    try:
        Name = request.POST['name']
        City = request.POST['city']
        Age = int(request.POST['age'])

        empobj = Employee.objects.create(name=Name, city = City, age=Age)
        empobj.save()

        return render(request,'index.html',{"msg": "Employee Added"})
    
    except Exception as e:
        print (e)
        return render(request,'index.html',{"msg": "Employee Can't be Added"})

