from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.template import RequestContext

# Create your views here.
from requests import session

from address import models


def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if models.idcheck(user_id=username,pwd=password) == 1:
            profile = "select * from workers where user_id = :userid and pwd = :password"
            request.session['user']= profile
            return redirect('index')
        else:
            msg1 = '로그인을 실패하였습니다.'
            msg2 = 'ID 및 PW를 다시 확인해주세요.'
            return render(request, 'login.html' , {'msg1':msg1,'msg2':msg2})
    else:

        return render(request, 'login.html')

def logout(request):
    if "profile" in request.session:
        del request.session['profile']
        return redirect('/')
    else:
        return redirect('/')



def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def banner(request):
    return render(request, 'banner.html')

def qna(request):
    return render(request, 'qna.html')

def user(request):
    return render(request, 'user.html')

def matching(request):
    return render(request, 'matching.html')

def money(request):
    return render(request, 'money.html')