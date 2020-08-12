from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.template import RequestContext

# Create your views here.
from requests import session

from address import models
from address.models import qnapage, connections, qnaviewpage, deleteqnapage, qnawrite, selzz


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
    qnalist = qnapage()
    qpage = []
    for e in qnalist:
        qvo = {"user_num":e[0],"user_id":e[1],"qna_num":e[2],"qtitle":e[3],"askcontent":e[4],"recontent":e[5],"qdate":e[6]}
        qpage.append(qvo)
    return render(request, 'qna.html' , {'qnapage':qpage})

def qnadetail(request):
    if request.method == "POST":
        qna_num = request.POST['qna_num']
        qnaview=qnaviewpage(qna_num=qna_num)
        list = []
        qvo = {"user_num":qnaview[0], "user_id":qnaview[1], "qna_num":qnaview[2], "qtitle":qnaview[3], "askcontent":qnaview[4], "recontent":qnaview[5], "qdate":qnaview[6]}

        return render(request, 'qnadetail.html' ,{'qnaview':qvo})
    else:
        return render(request, 'qna.html')

def deleteqna(request):
    qna_num = request.POST['qna_num']
    deleteqnapage(qna_num=qna_num)
    return redirect('qna')

def qnawritepage(request):
    qtitle = request.POST['qtitle']
    qna_num = request.POST['qna_num']
    recontent = request.POST['recontent']
    qnawrite(qtitle=qtitle,recontent=recontent, qna_num=qna_num)
    return redirect('qna')


def user(request):
    return render(request, 'user.html')

def matching(request):
    return render(request, 'matching.html')


def sel(request):
    sellist = selzz()
    selpage = []
    for e in sellist:
        svo = {"order_num": e[0],  "product_num": e[1], "user_num": e[2], "imp": e[3], "total": e[4],"order_date": e[5], "amount": e[6], "user_id": e[7]}
        selpage.append(svo)
    return render(request, 'sel.html', {'sel': selpage})