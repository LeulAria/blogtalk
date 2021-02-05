from django.contrib import admin
from .models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    prepopulated_fields = ({'slug': ('title',)})

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'created_on', 'post')
    list_filter = ("post", "author", "created_on")
    search_fields = ['created_on', 'body']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)