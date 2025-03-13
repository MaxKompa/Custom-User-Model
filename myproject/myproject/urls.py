from django.contrib import admin
from django.urls import path
from custom_user.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
]
