from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserForm


def home(request):
    return render(request, "loginapp/home.html")


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!")
            return redirect("Register")

        messages.error(request, "Please correct the highlighted errors.")
    else:
        form = UserForm()

    return render(request, "loginapp/Register.html", {"form": form})