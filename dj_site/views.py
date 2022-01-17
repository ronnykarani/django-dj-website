from django.shortcuts import render
from blog.models import Post
from mix.models import Video
from django.utils import timezone


# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
    context = {'posts': posts, }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})