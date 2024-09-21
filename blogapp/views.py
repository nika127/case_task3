from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, Subscription  # Импортируй свои модели

# Представление для главной страницы блога
def index(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'blogapp/index.html', {'posts': posts})

# Представление для создания нового поста
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_post = Post(title=title, content=content)
        new_post.save()
        return redirect('index')  # Перенаправляем на главную страницу
    return render(request, 'blogapp/create_post.html')

# Представление для добавления комментария
def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        content = request.POST.get('content')
        new_comment = Comment(post=post, content=content)
        new_comment.save()
        return redirect('index')  # Перенаправляем на главную страницу
    return HttpResponse(status=400)

# Представление для подписки на пользователя
def subscribe(request, user_id):
    if request.method == 'POST':
        subscription = Subscription(user_id=user_id)
        subscription.save()
        return redirect('index')  # Перенаправляем на главную страницу
    return HttpResponse(status=400)
