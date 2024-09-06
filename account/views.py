from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'account/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('/')
