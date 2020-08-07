from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

import cx_Oracle as ora

def connections():
    try:
        conn = ora.connect('project/kosmo64@192.168.0.119:1521/orcl', encoding='utf-8')
    except Exception as e:
        conn = "예외 발생"
        print(conn)
        print(e)
        return
    return conn

def idcheck(**key):
    conn = connections()
    cursor = conn.cursor()
    sql_idcheck = "select count(*) from workers where user_id = :userid and pwd = :password"
    try:
        cursor.execute(sql_idcheck,userid=key['user_id'],password=key['pwd'])
    except Exception as e:
        print('출력 오류', e)
    finally:
        idcount = cursor.fetchall()
        id = idcount[0][0] ==1
        cursor.close()
        conn.close()
    return id


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']