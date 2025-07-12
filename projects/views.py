from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            form.save_m2m()  # For saving many-to-many fields
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, created_by=request.user)
    tasks = Task.objects.filter(project=project)  # ✅ Added: fetch tasks for this project
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })


def home(request):
    return render(request, 'home.html')
