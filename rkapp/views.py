from django.db.models.query_utils import Q
from django.shortcuts import render ,HttpResponse ,redirect
from .models import Employee, Role, Department
# Create your views here.
def index(request):
  
  return render(request, 'index.html',)

def all_emp(request):
  emps=Employee.objects.all()
  context = {
        'emps': emps,
    }
  print(context)
  return render(request, 'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        dept_id = int(request.POST['dept'])
        role_id = int(request.POST['role'])
        phone = int(request.POST['phone'])
        bonus = int(request.POST['bonus'])
        hire_date = request.POST['hire_date']

        # Retrieve department and role instances
        department = Department.objects.get(pk=dept_id)
        role = Role.objects.get(pk=role_id)

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            dept=department,
            role=role,
            phone=phone,
            bonus=bonus,
            hire_date=hire_date
        )
        new_emp.save()
        return redirect('add_emp')
    elif request.method == 'GET':
        # Retrieve departments and roles for dropdowns
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'departments': departments,
            'roles': roles
        }
        return render(request, 'add_emp.html', context)
    else:
        return HttpResponse('An error occurred')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def edit_emp(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)

    if request.method == 'POST':
        emp.first_name = request.POST['first_name']
        emp.last_name = request.POST['last_name']
        emp.salary = request.POST['salary']
        emp.dept_id = request.POST['dept']
        emp.role_id = request.POST['role']
        emp.phone = request.POST['phone']
        emp.bonus = request.POST['bonus']
        emp.hire_date = request.POST['hire_date']
        emp.save()
        return redirect('all_emp')

    departments = Department.objects.all()
    roles = Role.objects.all()
    return render(request, 'edit_emp.html', {'emp': emp, 'departments': departments, 'roles': roles})


def remove_emp(request, emp_id=0):
  if emp_id:
      try:
          emp = Employee.objects.get(id=emp_id)
          emp.delete()
          return redirect('all_emp')
      except:
          return HttpResponse('An error occurred')  
    
  emps = Employee.objects.all()
  context ={
      'emps': emps
  }  
  return render(request, 'remove_emp.html',context)

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)

        context = {'emps': emps}
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An error occurred')

      