from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ("status", "created_on")
    search_fields = ['title', 'content']
    prepopulated_fields = ({'slug': ('title',)})


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
