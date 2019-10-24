from django.shortcuts import render,get_object_or_404  #render ben ekstraktimin e te dhenave te db dhe html e shfaq ne python
from .models import Post

# Create your views here.  

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #funksioni perdoret per te kapur nje rresht nga db
    return render(request, 'blog/post_detail.html', {'post': post})