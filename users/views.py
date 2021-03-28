from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)


		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Account has been update')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form':u_form,
		'p_form':p_form
	}

	return render(request, 'users/profile.html',context)