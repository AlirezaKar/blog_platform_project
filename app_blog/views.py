from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, PostImages, Category, SubCategory, Comment, User
from .forms import NewPostForm, CommentForm

def post_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request=request, template_name='blog/post_view.html', context=context)

def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        data = CommentForm(request.POST)
        if data.is_valid():
            form_data = data.cleaned_data
            username = form_data.get("email").split("@")[0]
            try:
                user = User.objects.get(username=username)
            except:
                user = User.objects.create(username=username, email=form_data.get("email"))

            comment = Comment.objects.create(text=form_data.get("text"), user=user, post=post)
        else:
            comments = Comment.objects.filter(post=post)
            context = {'post':post, 'form':form, 'comments':comments}
            print(form.errors.as_data())
            return render(request=request, template_name='blog/post_detail_view.html', context=context)
        
    elif request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        context = {'post':post, 'form':form, 'comments':comments}
        return render(request=request, template_name='blog/post_detail_view.html', context=context)
    
    try:
        comments = Comment.objects.filter(post=post)
        context = {'post':post, 'form':form, 'comments':comments}
        return render(request=request, template_name='blog/post_detail_view.html', context=context)
    except:
        redirect(post_view)
   
def new_post_view(request):
    post_form = NewPostForm()

    if request.method == 'POST':
        post_data = NewPostForm(request.POST)
        if post_data.is_valid():
                post_form_data = post_data.cleaned_data
                post = Post.objects.create(
                     title=post_form_data.get("title"),
                     text=post_form_data.get("text"),
                     user=post_form_data.get("user"),
                     status=post_form_data.get("status"),
                     category=post_form_data.get("category")
                )
                return redirect(post_view)
        
        else:
            context = {'post_form':post_form}
            return render(request=request, template_name='blog/new_post_view.html', context=context)
        
    elif request.method == 'GET':
        return render(request=request, template_name='blog/new_post_view.html', context={'post_form':post_form})
    
# def new_post_image_view(request):
#     image_form = PostImageForm()
#     if request.method == 'POST':
#         data = PostImageForm(request.POST)
#         if data.is_valid():
#             form_data = data.cleaned_data
#             image = PostImages.objects.create(post=form_data.get("post"), file=form_data.get("file"))

#             return redirect(post_view)
#         else:
#             print('Data is not valid!')
#             context = {'image_form':image_form}
#             return render(request=request, template_name='blog/new_post_image_view.html', context=context)

#     elif request.method == 'GET':
#         context = {'image_form':image_form}
#         return render(request=request, template_name='blog/new_post_image_view.html', context=context)    
