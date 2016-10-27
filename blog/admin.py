from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'image','imageone', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body','bodyone')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    pass
admin.site.register(Post, PostAdmin)



