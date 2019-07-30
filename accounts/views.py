from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username= request.POST['username']).exists():
                return render(request, 'signup.html', {'already': '이미 가입된 아이디입니다.'})
            else:
                user= User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                #회원가입을 하고 바로 로그인을 하게 만드는 것
                return redirect('home') #다 실행이 된다면 blog url로 간다
    return render(request, 'signup.html') #실패하면 머무르기

def login(request):
    if request.method == 'POST' :
        username= request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(request, username=username, password=password)
        #회원이 맞는지를 확인해주는 함수, 맞는지 아닌지 결과를 user에 담아준다.
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')

