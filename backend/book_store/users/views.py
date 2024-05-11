from django.shortcuts import render, redirect
from forms import SignupForm
from models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.get(number=form.cleaned_data.get("number"))
            if user != None:
                form.add_error("number", ValueError("number already exist"))
            else:
                user = User()
                user.name = form.cleaned_data.get("name")
                user.password = make_password(form.cleaned_data.get("password"))
                user.number = form.cleaned_data.get("number")
                User.objects.create(user)
                return redirect("/")

    else:
        form = SignupForm()
    
    return render(request, "users/signup.html", {"form": form})