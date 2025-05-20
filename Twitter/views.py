from django.http import HttpResponse
from .models import Tweet
from .forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, CommentLike, TweetLike
from django.http import JsonResponse
from django.db.models import Count, Q

# Create your views here.

def rough(request):
    return render(request, 'rough.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')

    for tweet in tweets:
        comments = tweet.comments.annotate(
            like_count=Count('likes', filter=Q(likes__is_like=True)),
            dislike_count=Count('likes', filter=Q(likes__is_like=False))
        )
        tweet.annotated_comments = comments

    return render(request, 'home.html', {'tweets': tweets})

def my_tweet_list(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_tweets.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, 'Tweet Posted Successfully')
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    like, created = TweetLike.objects.get_or_create(tweet=tweet, user=request.user)
    like.is_like = True
    like.save()
    return redirect('tweet_list')

@login_required
def dislike_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    like, created = TweetLike.objects.get_or_create(tweet=tweet, user=request.user)
    like.is_like = False
    like.save()
    return redirect('tweet_list')

@login_required
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(tweet=tweet, author=request.user, content=content)
            messages.success(request, 'Comment added successfully.')
    return redirect('tweet_list')

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = CommentLike.objects.get_or_create(comment=comment, user=request.user)

    if not created and like.is_like:
        like.delete()
    else:
        like.is_like = True
        like.save()

    return redirect('tweet_list')

@login_required
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = CommentLike.objects.get_or_create(comment=comment, user=request.user)

    if not created and not like.is_like:
        like.delete()
    else:
        like.is_like = False
        like.save()

    return redirect('tweet_list')



@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            messages.success(request, 'Tweet Updated Successfully')
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        messages.success(request, 'Tweet Deleted Successfully')
        return redirect('tweet_list')
    return render(request, 'home.html', {'tweet': tweet})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Login Successful')
            return redirect('tweet_list')
        else:
            for error in form.errors.values():
                messages.error(request, error)

    return render(request, 'registration/login.html', {'form': form})

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('tweet_list')
        else:
            for error in form.errors.values():
                messages.error(request, error)

    return render(request, 'registration/register.html', {'form': form})

@login_required
def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'profile.html', context)

