from django.shortcuts import render
from .forms import RocketBlogForm

# Create your views here.
def Home(request):
    form = RocketBlogForm
    if request.method == 'POST':
        form = RocketBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return render('home')
    return render(request, 'index.html', {'form':form})