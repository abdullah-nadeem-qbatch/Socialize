from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('R', 'Rather not say'),
    )
    RELATIONSHIP_STATUS = (
        ('I', 'In Relationship'),
        ('N', 'No Relationship'),
    )
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    #username = models.CharField(max_length=15, unique = True)
    #email = models.CharField(max_length=40, unique = True)
    #firstname = models.CharField(max_length=40)
    #lastname = models.CharField(max_length=40)
    #password = models.CharField(max_length=25)
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)
    relationshipStatus = models.CharField(max_length=1, choices=RELATIONSHIP_STATUS)
    address = models.TextField()
    workDesignation = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self', through='Friendship', symmetrical=False, 
        related_name='friend', blank=True
        )


class Chat(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatStartTime = models.DateTimeField()


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    messageContent = models.TextField()
    messageTime = models.DateTimeField()
    sentOrReceived = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postContent = models.TextField()
    noOfLikes = models.IntegerField(default=0)
    postTime = models.DateTimeField(verbose_name='Post Date', auto_now=True)


class Share(models.Model):
    shareTime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentContent = models.TextField()
    commentTime = models.DateTimeField(verbose_name='Comment Date', auto_now=True)


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    replyContent = models.TextField()
    replyTime = models.DateTimeField()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentReply = models.ForeignKey(CommentReply, on_delete=models.CASCADE)


class Friendship(models.Model):
    fromUser = models.ForeignKey(User, related_name='fromUser', on_delete=models.CASCADE)
    toUser = models.ForeignKey(User, related_name='toUser', on_delete=models.CASCADE)
