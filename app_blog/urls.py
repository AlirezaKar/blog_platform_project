from django.urls import path

from .views import post_detail_view, post_view, new_post_view

urlpatterns = [
    path('', view=post_view, name='post_view'),
    path('<int:id>', view=post_detail_view, name='post_detail_view'),    
    path('new_post', view=new_post_view, name='new_post_view'),
    # path('new_post_image', view=new_post_image_view, name='new_post_image_view'),
    
]