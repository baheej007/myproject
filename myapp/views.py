from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'myapp/home.html', {'posts': posts})



from .models import PostImage

def search_by_hashtag(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        images = PostImage.objects.filter(hashtags__icontains=query)  # Search for images with the hashtag
    else:
        images = PostImage.objects.all()  # If no query, show all images
    return render(request, 'myapp/search_results.html', {'images': images})
