from django.shortcuts import render   #render ben kalimin e kodit html ne python

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})