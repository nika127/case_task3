from django.contrib import admin
from .models import Tag, Post, Comment, Subscription

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subscription)
