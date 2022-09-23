from django.shortcuts import render
from . forms import SignUpForm
from . models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.list import ListView

def signUp(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})


def signIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signIn')

    
    return render(request, 'registration/login.html')

    #return render(request, 'registration/login.html')


def profile(request):
    current_user = request.user
    #pk1 = current_user
    #print(pk1)
    return render(request, 'registration/profile.html',{'user': current_user})


def home(request):
    pst = Post.objects.all()
    #print(pst)
    return render(request, 'home.html', {'post':pst})


def showPost(request):
    return render(request, 'post.html')


def uploadPost(request):
    #if request.method == 'POST':
    #    content = request.POST['content']
    #    current_user = request.user
    #    pst = Post.objects.create(current_user, content)
    #    pst.save()
    #    messages.info(request, 'Post Uploaded')
    #    return redirect('signIn')
    #import pdb
    #pdb.set_trace()

    if request.method == 'POST':
        user = request.user
        content = request.POST['content']

        new_post = Post.objects.create(user=user, postContent=content)
        new_post.save()

        return redirect('/home/')
    else:
        return redirect('/post/')
    
    #current_user_pk = Post.objects.filter(user = current_user.pk)
    #return render(request, 'post.html', )


def likePost(request, pk):
    post = Post.objects.get(id = pk)
    post.noOfLikes = post.noOfLikes + 1
    post.save()
    return redirect('/home')

def unlike(request, pk):
    post = Post.objects.get(id = pk)
    post.noOfLikes = post.noOfLikes - 1
    if post.noOfLikes < 0:
        post.noOfLikes = 0
    post.save()
    return redirect('/home')


def commentPost(request, pk):
    post = Post.objects.get(id = pk)
    comment = post.comment_set.all()
    #print(comment.values())
    context = {'post': post, 'comment': comment}
    return render(request, 'postthread.html', context)

def showAddComment(request, pk):
    post = Post.objects.get(id = pk)
    content = {'post':post}
    return render(request, 'addcomment.html', content)


def addComment(request, pk):
    commentContent = request.POST['comment']
    pst = Post.objects.get(id = pk)
    cmt = Comment.objects.create(post = pst, commentContent = commentContent)
    comment = Comment.objects.filter(post = pst)
    
    #print(commentContent)
    return render(request, 'postthread.html', {'comment':comment, 'post':pst})

def deleteComment(request):
    return HttpResponse('hello')
