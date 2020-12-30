from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})
    
def blogpost(request, id):
    if id == 1 or id == 2 or id == 3 or id == 4:
        post = Blogpost.objects.filter(post_id = id)[0]
        return render(request, 'blog/blogpost.html', {'post' : post})
    else:
        return HttpResponse(
            '''
            <h2>Sorry You landed the wrong Page!!</h2> <br>
            <a href="/shop">Go to Home Page</a><br>
            <a href="/blog">Go to Blog Page</a>
            '''
            ) 