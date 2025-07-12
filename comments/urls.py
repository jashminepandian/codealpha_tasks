from django.urls import path
from . import views

urlpatterns = [
    path('task/<int:task_id>/', views.task_detail_with_comments, name='task_detail'),
]
