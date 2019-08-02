from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('polls/index.html')
    print("this: ", template)
    return render(request, 'polls/index.html')
    
def about(request):
    template = loader.get_template('polls/about.html')
    return render(request, 'polls/about.html')
    
def colorgame(request):
    template = loader.get_template('polls/colorgame.html')
    return render(request, 'polls/colorgame.html')
    
def blog(request):
    template = loader.get_template('polls/blog.html')
    return render(request, 'polls/blog.html')
    