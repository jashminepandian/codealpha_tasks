from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),

]






