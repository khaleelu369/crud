from django.shortcuts import render,redirect
from .forms import employeeform
from .models import employee,position
# Create your views here.
def employee_list(request):
    context = {'employee_list':employee.objects.all()}
    return render(request,"employee_list.html",context)

def employee_form(request,id=0):
  if request.method == "GET":
    if id==0:  
      form=employeeform()
    else:
       Employee=employee.objects.get(pk=id)
       form=employeeform(instance=Employee)
    return render(request,"employee_form.html",{'form':form})
  else:
     if id==0:
        form=employeeform(request.POST)
     else:
        Employee=employee.objects.get(pk=id)
        form=employeeform(request.POST,instance=Employee)
     if form.is_valid():
        form.save()
     return redirect('list')   
def employee_delete(request,id):
    Employee=employee.objects.get(pk=id)
    Employee.delete()
    return redirect('list') 

