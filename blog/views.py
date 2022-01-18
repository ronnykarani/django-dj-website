from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def blog(request):
    return render(request, 'blog/post_list.html', {})