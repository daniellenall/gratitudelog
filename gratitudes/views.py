from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from django.utils import timezone
from .models import Gratitude

@login_required
def createnew(request):
    if request.method == 'POST':
        if request.POST['title']:
            gratitude = Gratitude()
            gratitude.title = request.POST['title']
            gratitude.date = timezone.datetime.now()
            gratitude.author = request.user
            gratitude.save()
            return redirect('home')
        else: 
            return render(request, 'gratitudes/new.html', {'error': 'Please enter something '})
    else:
        return render(request, 'gratitudes/new.html')

def home(request):

    if request.user.is_authenticated:
        gratitudes = Gratitude.objects.order_by('date')
    else:
        return render(request, 'accounts/login.html')

    return render(request, 'gratitudes/home.html', {'gratitudes': gratitudes})