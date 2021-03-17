from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


# method for register.
def register(request):
	if request.method == 'POST':
		formulir = UserRegisterForm(request.POST)
		if formulir.is_valid():
			formulir.save()
			username = formulir.cleaned_data.get('username')
			messages.success(request,f'Account has been created. Login Now')
			return redirect('login')
	else :
		formulir = UserRegisterForm()
	return render(request,'users/register.html',{'form':formulir})


@login_required
def profile(request):
	return render(request, 'users/profile.html')