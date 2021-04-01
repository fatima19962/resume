from django.shortcuts import render
from .models import Resume,Post
from django.views.generic import ListView
from resume.forms import ContactMe



# Create your views here.
#from django.http import HttpResponse



def home(request):
    #return HttpResponse('<h1>HOME PAGE<h1/>  ')
    return render(request,'resume/home.html')


def about(request):
      resume = Resume.objects.get(pk=1)
      return render(request,'resume/about.html',{"resume":resume})

def blog(request):
    post_objects = Post.objects.all().order_by('-date')
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
          post_ojects=post_objects.filter(title__icontains=item_name)

    return render(request,'resume/blog.html',{'post_objects':post_objects})

# def blog(request):
#       context = {
#         'posts':Post.objects.all()
#       }
#       resume = Resume.objects.get(pk=1)
#       return render(request,'resume/blog.html',context)

class PostListView(ListView):
   model = Post
   template_name = 'resume/blog.html'
   context_object_name = 'posts'
   ordering = ['-date']

def form(request):
    form = ContactMe()
    return render(request,'resume/process-form.html',{'form':form})

def portfolio(request):
    #return HttpResponse('<h1>HOME PAGE<h1/>  ')
    return render(request,'resume/portfolio.html')

def blog_post(request):
    #return HttpResponse('<h1>HOME PAGE<h1/>  ')
    return render(request,'resume/blog-post.html')