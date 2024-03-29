from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.filter(username=form.data['username']).first()
            profile = Profile(user=user)
            profile.save()
            return redirect('/login')
        else:
            return render(request, 'core/register.html', {'form': form})
    form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'core/login.html',
                          {'message': 'Wrong Credentials'})
    else:
        return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'core/profile.html')
