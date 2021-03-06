from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.template import RequestContext

# Create your views here.
from requests import session

from address import models
from address.models import qnapage, connections, qnaviewpage, deleteqnapage, qnawrite, selzz, banuser, banuser2,banuser3,selchartdate


def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if models.idcheck(user_id=username,pwd=password) == 1:
            profile = "select * from workers where user_id = :userid and pwd = :password"
            request.session['user']= profile
            sellist = selzz()
            selpage = []
            for e in sellist:
                svo = {"order_num": e[0],  "product_num": e[1], "user_num": e[2], "imp": e[3], "total": e[4],"order_date": e[5], "amount": e[6], "user_id": e[7]}
                selpage.append(svo)
            return render(request, 'sel.html', {'sel': selpage})
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
    sellist = selzz()
    selpage = []
    for e in sellist:
        svo = {"order_num": e[0],  "product_num": e[1], "user_num": e[2], "imp": e[3], "total": e[4],"order_date": e[5], "amount": e[6], "user_id": e[7]}
        selpage.append(svo)
    return render(request, 'sel.html', {'sel': selpage})

def register(request):
    return render(request, 'register.html')

def banner(request):
    banlist = banuser()
    bpage = []
    for e in banlist:
        bvo = {"report_num": e[0], "user_num": e[1], "user_id": e[2], "report_user_num": e[3], "reason": e[4]}
        bpage.append(bvo)
    return render(request, 'banner.html', {'bpage':bpage})

def banner2(request):
    banlist = banuser2()
    boardpage = []
    for e in banlist:
        bvo = {"report_board_num": e[0], "user_num": e[1], "user_id": e[2], "board_num": e[3], "reason": e[4]}
        boardpage.append(bvo)
    return render(request, 'banner2.html', {'boardpage':boardpage})

def banner3(request):
    banlist = banuser3()
    bwritten = []
    for e in banlist:
        bvo = {"report_comment_num": e[0], "user_num": e[1], "user_id": e[2], "board_num": e[3], "comment_num": e[4],"reason": e[5]}
        bwritten.append(bvo)
    return render(request, 'banner3.html', {'bcommentpage':bwritten})

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

def sel(request):

    sellist = selzz()
    selpage = []
    for e in sellist:
        svo = {"order_num": e[0],  "product_num": e[1], "user_num": e[2], "imp": e[3], "total": e[4],"order_date": e[5], "amount": e[6], "user_id": e[7]}
        selpage.append(svo)
    return render(request, 'sel.html', {'sel': selpage})

def chart(request):
    list = models.selchartdate()
    datedata = ['x']
    paydata = ['Amount']
    for i in list:
        datedata.append(i[1])

        paydata.append(i[0])
    chart_data = dict()
    chart_data['datedata'] = datedata
    chart_data['paydata'] = paydata
    return render(request, "chartserver.html",{"chart_data":[chart_data]})
