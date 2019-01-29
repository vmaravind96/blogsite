from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for {}'.format(username))
            return redirect('myblog')
    else:
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')
