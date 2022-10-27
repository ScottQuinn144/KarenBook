from django.shortcuts import render, get_object_or_404
from .models import Profile, Posts, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView


def commenting(request, id):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comments = comment_form.save(commit=False)
        comments.post = Posts.objects.get(id=id)
        comments.user = request.user
        print(comment_form)
        comments.save()
        return redirect("dashboard")
    context = {'comment_form': comment_form}
    return render(request, "socials/comment.html", context)


def dashboard(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect("dashboard")
    context = {'form': form}
    return render(request, "dashboard.html", context)


def index(request):
    return render(request, "index.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "socials/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    comment_form = CommentForm(request.POST or None)
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


def delete(request, id):
    delete_post = Posts.objects.get(id=id)
    profile = request.user.profile
    delete_post.delete()
    return render(request, "socials/profile.html", {"profile": profile})


def PostEdit(request, id):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = Posts.objects.get(id=id)
        post.delete()
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect("dashboard")
    context = {'form': form}
    return render(request, "socials/edit.html", context)
