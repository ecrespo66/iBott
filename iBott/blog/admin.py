from django.contrib import admin
from blog.models import *

# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("mail",)


admin.site.register(Subscriber, SubscriberAdmin)


class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", 'category', 'creation_date', 'creator')


admin.site.register(Post, PostsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", 'creation_date', 'creator')


admin.site.register(Comment, CommentAdmin)


class CategoriesAdmin(admin.ModelAdmin):

    list_display = ("name",)

admin.site.register(Category,CategoriesAdmin)