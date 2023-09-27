from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'get_category', 'type', 'timePost', 'title', 'textPost')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'subscribe_count')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
