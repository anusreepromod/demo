from django.shortcuts import render
from projectapp.models import *

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        login_obj = logins(email=email, password=password)
        login_obj.save()
        return render(request, 'login.html', {'msg': 'created'})
    return render(request, 'login.html')
