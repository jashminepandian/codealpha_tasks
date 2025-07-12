from django.urls import path
from . import views

urlpatterns = [
    path('<int:project_id>/create/', views.create_task, name='create_task'),
    path('<int:project_id>/tasks/', views.task_list, name='task_list'),  # if implemented
]



