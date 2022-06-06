from django.shortcuts import render,redirect
from .forms import RocketBlogForm

# Create your views here.
def Home(request):
    form = RocketBlogForm
    if request.method == 'POST':
        form = RocketBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'index.html', {'form':form})