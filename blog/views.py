from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blog, Comment
from .forms import CommentForm


def all_blogs(request):
    blogs = Blog.objects.order_by('-pub_date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(post=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if not request.user.is_authenticated:
                comment.name = 'Аноним'
            comment.post = blog
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'blog': blog, 'comments': comments, 'form': form})
#
#     return render(request, 'blog/detail.html', {'blog': blog})
#
#
# def post_detail(request, blog_id):
#     post = get_object_or_404(Blog, id=blog_id)
#     comments = post.comments.all()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             if not request.user.is_authenticated:
#                 comment.name = 'Аноним'
#             comment.post = post
#             comment.save()
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = CommentForm()
#     return render(request, 'detail.html', {'post': post, 'comments': comments, 'form': form})
