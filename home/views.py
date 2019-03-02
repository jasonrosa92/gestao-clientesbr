from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def my_home(request):
    return render(request, 'home.html')
