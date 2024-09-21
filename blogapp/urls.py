from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница блога
    path('create_post/', views.create_post, name='create_post'),  # Создание поста
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),  # Добавление комментария
    path('subscribe/<int:user_id>/', views.subscribe, name='subscribe'),  # Подписка на пользователя
]
