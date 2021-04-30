from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from itertools import chain
from django.http import JsonResponse
import json

def index(request):
    po = post.objects.all().order_by('time').reverse()
    for posta in po:
        posta.likes = Like.objects.filter(post=posta.id).count()
        posta.save()
    p=Paginator(po,10)
    print(p.num_pages)
    page_num=request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage :
        page=p.page(1)

    return render(request, "network/index.html",{
      "po" : page
    })

def allpost(request):
    userp = request.user.username
    posts = post.objects.filter(user=userp).order_by('time').reverse()
    return render(request, "network/allpost.html", {
        "po": posts,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new(request):
    if request.method == "POST":
        text = request.POST['content']
        new = post(content=text,user=request.user.username)
        new.save()
        return redirect(index)
    else:
        return render(request, "network/new.html")

def like(request,lid):
    posti=post.objects.get(id=lid)

    if request.method == "GET":
        return JsonResponse(posti.serialize())


    if request.method=="PUT":
        data=json.loads(request.body)
        if data.get("like"):
            Like.objects.create(user=request.user,post=posti)
            posti.likes=Like.objects.filter(post=posti).count()

        else:
            Like.objects.filter(user=request.user,post=posti).delete()
            posti.likes=Like.objects.filter(post=posti).count()
        posti.save()

        return HttpResponse(status=204)

def profile(request,username):
    user = User.objects.get(username=username)
    posts = post.objects.filter(user=username).order_by('time').reverse()
    followers = user.followers.all()
    foll=user.following.all()
    is_follower = False
    for item in followers:
        if request.user.username == item.follower.username:
            is_follower = True

    p = Paginator(posts, 10)
    print(p.num_pages)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {
        'username': username,
        'posts': page,
        'followers': followers,
        'is_follower': is_follower,
        'following' : foll
    }

    return render(request, "network/profile.html", context)

def follow(request,target):
    targeta = User.objects.get(username=target)
    request.user.follow(targeta)
    return redirect('index')


def unfollow(request, target):
    targeta = User.objects.get(username=target)
    request.user.unfollow(targeta)
    return redirect('index')

def followpost(request):
    if request.method == 'GET':

        posts = []

        for i in profilei.objects.filter(follower=request.user):
            posts = list(chain(posts, post.objects.filter(user=i.following)))

        for posta in posts:
            posta.likes = Like.objects.filter(post=posta.id).count()
            posta.save()

        p = Paginator(posts, 10)
        print(p.num_pages)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        return render(request, "network/follow.html", {
              'fpost': page,
        })
    ''''
        if request.method == 'GET':
            currentuser = get_object_or_404(User, username=username)
            follows = profilei.objects.filter(follower=currentuser)
            posts = post.objects.all().order_by('id').reverse()
            l = []
            for p in posts:
                for follower in follows:
                    if follower.following == p.user:
                        l.append(p)
                        print(follower.following)
                        print('hi')
                        print(l)

            if not follows:
                return render(request, 'network/follow.html', {'message': "jknjnjnnj"})


            return render(request, 'network/follow.html', {'posts': l})
'''


def edit(request, post_id):
    j=post.objects.get(id=post_id)

    if request.method == "PUT":
        data=json.loads(request.body)
        if data.get("pos") is not None:
            j.content=data["pos"]
        j.save()
        return  HttpResponse(status=204)