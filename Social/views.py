from django.shortcuts import render
from .models import Profile, Posts
from .forms import PostForm
from django.shortcuts import render, redirect


def dashboard(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("dashboard")
    return render(request, "dashboard.html", {"form": form})


def index(request):
    return render(request, "index.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "socials/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "socials/profile.html", {"profile": profile})
