from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post, PostImages, Category, SubCategory, Comment

def post_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request=request, template_name='blog/post_view.html', context=context)

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
        context = {'post':post}
        return render(request=request, template_name='blog/post_detail_view.html', context=context)
    except Post.DoesNotExist:
        return render(request=request, template_name='blog/post_view.html', context={'error':'Object not found.'})