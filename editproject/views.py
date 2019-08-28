from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
# from accounts.forms import 
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.template import RequestContext
from django.shortcuts import render
from .models import Employee
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,

)

from .forms import UserRegisterForm

# Create your views here.
def login(request):
    return render(request,'editproject/login.html')
def index(request):
    # user_details = Employee.objects.all()
    return render(request,'editproject/index.html',{})
    # return render(request,'editproject/index.html', {})
# def register(request):
#     return render(request,'editproject/register.html', {})
def userdetails(request):
    user_details = Employee.objects.all()
    return render(request,'editproject/userdetails.html',{'users':user_details})

def delete (request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect("http://127.0.0.1:8000/userdetails.html")

# def index(request):
#     Password = [1,2,3,4,5]
#     UserName = 'hero'
#     args = {'UserName' :UserName, 'Password':Password}
#     return render(request, 'editproject/index.html',args)

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect('/account/profile')
#         else:
#             form = PasswordChangeForm(user = request.user)
#             args = {'form':form}
#             return HttpResponse('editproject/change_password.html',args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        # else:
        #     messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'editproject/change_password.html', {
        'form': form
    })

# from .models import Employee

# def register_user(request):
#         print ("success")
#         name = request.POST["name"]
#         address = request.POST["address"]
#         email = request.POST["email"]
#         phone_no = request.POST["phone_no"]
#         username = request.POST["username"]
#         password = request.POST["password"]

#         employee_user = Employee(name=name,address=address,email=email,phone_no=phone_no,username=username,password=password)
#         employee_user.save()
#         return render (request, "editproject/register.html")
       # post.save()


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "editproject/register.html", context)


 


     