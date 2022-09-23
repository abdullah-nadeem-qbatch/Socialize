from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Share)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(Like)
admin.site.register(Friendship)

