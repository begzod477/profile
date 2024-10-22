from django.shortcuts import render, get_object_or_404
from .models import User

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def profile(request, profile_id):
    user = get_object_or_404(User, id=profile_id)
    return render(request, 'profile.html', {'user': user})
