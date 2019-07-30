from django.shortcuts import render, get_object_or_404, redirect #이거 까먹지 말기
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogPost
#import 잊지 말기
# Create your views here.

def home(request):
    blogs=Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs, 'posts': posts})

def detail(request,blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'details':details})

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now() #현재 시간 넣어주는거, import해야함
    blog.save() #객체.delete()는 지워라
    return redirect('/blog/'+str(blog.id))#위에 다 처리하고 url로 넘겨라

def delete(request,details_id):
    post = get_object_or_404(Blog, pk= details_id)
    post.delete()
    return redirect('home')

def update(request, details_id):
    changewhat= get_object_or_404(Blog, pk= details_id)
    form= BlogPost(request.POST, instance=changewhat)

    if form.is_valid():
        post = form.save(commit=False)
        post.pub_date = timezone.now()
        post.save()
        return redirect('detail', post.id)

    return render(request, 'new.html', {'form' : form})

def blogpost(request):
  
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    else:
        form= BlogPost()
        return render(request, 'new.html', {'form':form})