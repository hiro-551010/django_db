from django.shortcuts import render
from .forms import UserForm
from .models import User
from .applications.sele import main

def index(request):
    form = UserForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            form.save()
            main()
            

    return render(request, 'db/index.html', context)


def checkusers(request):
    data = User.objects.all()
    context = {
        'data': data
    }
    return render(request, 'db/user.html', context)


