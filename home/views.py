from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import BlogPost
from .forms import UserRegistrationForm, UserLoginForm, BlogPostForm


def index(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("This is the about page.")


def services(request):
    return HttpResponse("This is the services page.")


def contact(request):
    return HttpResponse("This is the contact page.")


# Registration View
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)


# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)


# Logout View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')
    return redirect('home')


# Create Post View
@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    
    context = {'form': form, 'title': 'Create New Post'}
    return render(request, 'create_post.html', context)


# Post Detail View
def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {'post': post}
    return render(request, 'post_detail.html', context)


# Edit Post View
@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    # Check if user is the author
    if request.user != post.author:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    
    context = {'form': form, 'post': post, 'title': 'Edit Post'}
    return render(request, 'edit_post.html', context)


# Delete Post View
@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    # Check if user is the author
    if request.user != post.author:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('home')
    
    context = {'post': post}
    return render(request, 'delete_post.html', context)

