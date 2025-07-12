from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from tasks.models import Task
from .models import Comment
from django.contrib.auth.decorators import login_required

@login_required
def task_detail_with_comments(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()

    return render(request, 'comments/task_detail.html', {
        'task': task,
        'comments': comments,
        'form': form,
    })
