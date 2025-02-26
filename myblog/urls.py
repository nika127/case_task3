from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls')),  # Убедись, что у тебя есть файл urls.py в blogapp
    path('', include('blogapp.urls')),  # Перенаправление корня на блог
]
