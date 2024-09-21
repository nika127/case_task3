from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribed_to')

    def __str__(self):
        return f'{self.user.username} subscribes to {self.subscribed_to.username}'
