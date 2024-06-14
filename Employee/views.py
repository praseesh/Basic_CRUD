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

def display (request):
    empdtls = Employee.objects.all()
    return render (request,"index.html",{'emp':empdtls})

# Employee.objects.all()               :- fetch all records
# Employee.objects.filter(name='abc')  :-
# Employee.objects.get(id=1)           :- Fetch only single record


def delete(request):
    if request.method == 'POST':
        empname = request.POST.get('name', '')
        empdtls = Employee.objects.filter(name=empname)
        if empdtls.exists():
            empdtls.delete()
            return render(request, 'index.html', {"msg": "Deleted"})
        else:
            return render(request, 'index.html', {"msg": "NO RECORDS FOUND!"})

    

def update(request):
    # update using filter
    try:
        oldname = request.POST["oldname"]
        newname = request.POST["newname"]
        emp = Employee.objects.filter(name=oldname)
        if emp.exists():
            emp.update(name=newname)
            return render (request,"index.html",{'msg1':"Updated"})
        else:
            return render(request,"index.html",{'msg1':"No records found"})
        
    except Exception as e:
        print(e)
        return render(request,"index.html",{'msg1':"Not Updated"})


