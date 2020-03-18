from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import *
from .form import EmployeeForm,EmployeeFormBU,EmployeeFormHR,EmployeeFormFinance
def home(request):
    return render(request,'home.html')


@login_required
def candidate_List_delivery(request):
    obj=Employee.objects.all()
    context={
        'object':obj
    }
    return render(request,'index.html',context)


@login_required
def candidate_List2_BU(request):
    obj=Employee.objects.filter(Actions='Approved',Employement_Type='External')
    context={
        'object':obj
        }
    return render(request,'index2.html',context)

@login_required
def candidate_List1_HR(request):
    obj=Employee.objects.filter(Actions='Approved',Employement_Type='Internal')
    obj1=Employee.objects.filter(Actions='Approved',Employement_Type='Bench')
    obj2=Employee.objects.filter(Actions4='Approved',Employement_Type='External')
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'index1.html',context)
@login_required
def candidate_List1_Finance(request):

    obj=Employee.objects.filter(Actions2='Approved',Employement_Type='External')
    context={
        'object':obj,

    }
    return render(request,'index3.html',context)

@login_required
def candidate_view_Delivery(request, id):
        obj= get_object_or_404(Employee, id=id)
        return render(request, 'candidate_details_Delivery.html', {'object':obj})
@login_required
def candidate_view_HR(request, id):
        obj= get_object_or_404(Employee, id=id)
        return render(request, 'candidate_details_HR.html', {'object':obj})
@login_required
def candidate_view_BU(request, id):
        obj= get_object_or_404(Employee, id=id)
        return render(request, 'candidate_details_BU.html', {'object':obj})
@login_required
def candidate_view_Finance(request, id):
        obj= get_object_or_404(Employee, id=id)
        return render(request, 'candidate_details_Finance.html', {'object':obj})



def approve(request):
    return render(request,'approve.html')


def disapprove(request):
    return render(request,'DisApprove.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #if user.username=='adithy'

        if user.username=='Delivery':
            if user.is_active:
                login(request,user)
                return redirect('/candidate_List_delivery')
            else:
                return HttpResponse("Your account was inactive.")
        elif user.username=='BU':
                if user.is_active:
                    login(request,user)
                    return redirect('/candidate_List2_BU')
        elif user.username=='HR':
                if user.is_active:
                    login(request,user)
                    return redirect('/candidate_List1_HR')
        elif user.username=='Finance':
                    if user.is_active:
                        login(request,user)
                        return redirect('/candidate_List1_Finance')

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})



def candidate_update_delivery(request, id):

        obj= get_object_or_404(Employee, id=id)
        form=EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/candidate_List_delivery')

        return render(request, 'candidate_update_delivery.html', {'form':form})

def candidate_update_HR(request, id):

        obj= get_object_or_404(Employee, id=id)
        form=EmployeeFormHR(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/candidate_List1_HR')

        return render(request, 'candidate_update_HR.html', {'form':form})

def candidate_update_finance(request, id):

        obj= get_object_or_404(Employee, id=id)
        form=EmployeeFormFinance(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/candidate_List1_Finance')

        return render(request, 'candidate_update_HR.html', {'form':form})



def candidate_update_BU(request, id):

        obj= get_object_or_404(Employee, id=id)
        form=EmployeeFormBU(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/candidate_List2_BU')

        return render(request, 'candidate_update_BU.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
