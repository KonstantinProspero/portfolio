from django.shortcuts import render
from .models import Project
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})



def post_like(request, post_id):
    post = get_object_or_404(Project, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

def post_dislike(request, post_id):
    post = get_object_or_404(Project, id=post_id)
    post.dislikes += 1
    post.save()
    return JsonResponse({'dislikes': post.dislikes})