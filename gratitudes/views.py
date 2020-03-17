from django.shortcuts import render, redirect, get_object_or_404
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

def delete(request, id):
    item = get_object_or_404(Gratitude, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('home')


def home(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        gratitudes = Gratitude.objects.filter(author=logged_in_user)
    else:
        return render(request, 'accounts/login.html')

    return render(request, 'gratitudes/home.html', {'gratitudes': gratitudes})