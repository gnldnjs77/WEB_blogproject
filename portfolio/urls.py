from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.portfolio,name="portfolio"),
    path('<int:portfolio_id>', views.show, name="show"),
    path('add', views.add, name='add'),
    path('adding', views.adding, name='adding'),

]