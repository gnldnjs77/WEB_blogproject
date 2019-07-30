from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from django.utils import timezone
# Create your views here.

def portfolio(request):
    portfolios=Portfolio.objects
    return render(request, 'portfolio.html',{'portfolios':portfolios})

def show(request, portfolio_id):
    shows=get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'show.html',{'shows':shows})

def add(request):
    return render(request,'add.html')

def adding(request):
    portfolio=Portfolio()
    portfolio.title=request.GET['title']
    portfolio.description=request.GET['description']
    portfolio.pub_date=timezone.datetime.now() #현재 시간 넣어주는거, import해야함
    portfolio.save() #객체.delete()는 지워라
    return redirect('/portfolio/')#위에 다 처리하고 url로 넘겨라

# def delete(request,portfolio_id):
#     Portfolio.objects.get(pk=portfolio_id).delete()
#     return redirect('/portfolio/')