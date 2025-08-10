from django.contrib import admin
from .models import Post, PostImages, Category, SubCategory, Comment

admin.sites.AdminSite.site_title = 'Admin'
admin.sites.AdminSite.site_header = ' Blog Admin'
admin.sites.AdminSite.index_title = 'Blog'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status']
    list_display_links = ['title', 'user']
    list_filter = ['status', 'date_created', 'date_modified']
    list_editable = ['status']
    search_fields = ['title', 'text']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name', 'description']
    search_fields = ['name', 'description']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category']
    list_display_links = ['name', 'parent_category']
    search_fields = ['name']

@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ['post']
    list_display_links = ['post']
    list_filter = ['date_created', 'date_modified']
    search_fields = ['post']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = []