from django import forms 

from .models import Post, PostImages

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'user', 'status', 'category'] 
        
class CommentForm(forms.Form):
    email = forms.CharField(max_length=40, widget=forms.EmailInput, required=True)
    text = forms.CharField(widget=forms.Textarea)

# class PostImageForm(forms.Form):
#     class Meta:
#         model = PostImages
#         fields = ['post', 'file']

# FIXME: Data input will not be valid