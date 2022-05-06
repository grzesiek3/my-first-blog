from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data = {'posts':posts}
    return render(request, 'post_list.html', data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {'post':post}
    return render(request, 'post_detail.html', data)

def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        data = {'form': form}
    return render(request, 'post_edit.html', data)