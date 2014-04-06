from django.contrib import admin
from posts.models import Post, Reply


class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]


admin.site.register(Post, PostAdmin)