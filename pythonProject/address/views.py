from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

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