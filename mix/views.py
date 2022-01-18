from django.shortcuts import render

# Create your views here.
def mix(request):
    return render(request, 'mix/mix_list.html', {})