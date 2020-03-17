from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username is taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords dont match'})
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])

            return render(request, 'accounts/login.html', {'error': 'Success!'})
        
        else:
            return render(request, 'accounts/login.html', {'error': 'Please enter valid login details'})

    
    
    else:   
        return render(request, 'accounts/login.html')

def logoutview(request):
    logout(request)
    return redirect('home')