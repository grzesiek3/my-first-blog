from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data = {'posts':posts}
    return render(request, 'post_list.html', data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {'post':post}
    return render(request, 'post_detail.html', data)