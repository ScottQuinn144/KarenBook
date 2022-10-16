from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "dashboard.html")


def index(request):
    return render(request, "index.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "socials/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "socials/profile.html", {"profile": profile})
