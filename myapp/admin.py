from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3  # Number of extra empty image fields displayed by default

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(PostImage)
