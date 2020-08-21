"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from address.views import *
import address.views
urlpatterns = [
    path('banner/', address.views.banner ,name='banner'),
    path('banner2/', address.views.banner2 ,name='banner2'),
    path('banner3/', address.views.banner3 ,name='banner3'),
    path('', address.views.login ,name='login'),
    path('logout', address.views.logout ,name='logout'),
    path('index', address.views.index ,name='index'),
    path('qna/', address.views.qna ,name='qna'),
    path('deleteqna/', address.views.deleteqna ,name='deleteqna'),
    path('qnadetail/', address.views.qnadetail ,name='qnadetail'),
    path('qnawritepage/', address.views.qnawritepage ,name='qnawritepage'),
    path('user/', address.views.user ,name='user'),
    path('sel/', address.views.sel ,name='sel'),
    path('sel/chart/', address.views.chart),
]
