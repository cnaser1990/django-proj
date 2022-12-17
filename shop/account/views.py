from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

class UserRegisterView(View):
    
    def get(self,request):
        form=UserRegisterForm
        return render(request , "account/register.html", {'form':form})
    
    def post(self , request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'] , cd['email'] , cd['password'])
            messages.success(request , 'your registration was successfull' , 'success')
            return redirect ('food_list')
        messages.error(request , 'your registration was not successfull' , 'danger')
        return render(request , "account/register.html", {'form':form})
    
        