from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('list/', views.project_list, name='project_list'),
    path('detail/<int:project_id>/', views.project_detail, name='project_detail'),  # ✅ Add this
    path('', views.project_list, name='project_list'),
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),  # 👈 new route
]


