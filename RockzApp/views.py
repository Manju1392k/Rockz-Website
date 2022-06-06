from django.shortcuts import render,redirect
from .forms import RocketBlogForm
from .models import RocketBlog

from django.contrib import messages

# Create your views here.
def Home(request):
    form = RocketBlogForm
    if request.method == 'POST':
        form = RocketBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Blog has been added successfully')
            return redirect('home')
    return render(request, 'index.html', {'form':form})

def Blogs(request):
    blogs = RocketBlog.objects.all
    return render(request, 'blogs.html', {'blogs':blogs})