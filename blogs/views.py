from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'blogs/home.html',{'blogs':blogs})

@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body']:
            blog = Blog()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.url = request.POST['url']
            blog.image = request.FILES['image']
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('/blogs/' + str(blog.id))

        else :
            return render(request, 'blogs/create.html',{'error':'Title and Body are required to create.'})
    return render(request, 'blogs/create.html')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html',{'blog':blog})

@login_required
def edit(request, blog_id):
    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.url = request.POST['url']
        blog.image = request.FILES['image']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blogs/' + str(blog.id))

    else :
        return render(request, 'blogs/<int:blog_id>/edit.html',{'error':'Title and Body are required to edit.'})
    return render(request, 'blogs/edit.html')
