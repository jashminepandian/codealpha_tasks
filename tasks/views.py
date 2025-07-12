from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from projects.models import Project
from django.contrib.auth.decorators import login_required

@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form, 'project': project})

@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id, created_by=request.user)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks/task_list.html', {'project': project, 'tasks': tasks})

