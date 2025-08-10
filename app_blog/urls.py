from django.urls import path

from .views import post_detail_view, post_view

urlpatterns = [
    path('', view=post_view, name='post_view'),
    path('<int:id>', view=post_detail_view, name='post_detail_view'),    
]