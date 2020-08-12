from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

import cx_Oracle as ora
from matplotlib.backend_bases import cursors


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
        cursor.execute(sql_idcheck, userid=key['user_id'], password=key['pwd'])
    except Exception as e:
        print('출력 오류', e)
    finally:
        idcount = cursor.fetchall()
        id = idcount[0][0] == 1
        cursor.close()
        conn.close()
    return id


def qnapage():
    conn = connections()
    cursor = conn.cursor()
    sql_qnalist = "select * from qna order by qna_num asc"
    try:
        cursor.execute(sql_qnalist)
    except Exception as e:
        print('출력오류', e)
    finally:
        qna = cursor.fetchall()
        cursor.close()
        conn.close()
    return qna


def qnaviewpage(**key):
    conn = connections()
    cursor = conn.cursor()
    sql_qnaview = "select * from qna where qna_num = :qna_num"
    try:
        cursor.execute(sql_qnaview, qna_num=key['qna_num'])
    except Exception as e:
        print('출력오류', e)
    finally:
        qnaview = cursor.fetchone()
        cursor.close()
        conn.close()
    return qnaview


def deleteqnapage(**key):
    conn = connections()
    cursor = conn.cursor()
    sql_del = "delete from qna where qna_num = :qna_num"
    try:
        cursor.execute(sql_del, qna_num=key['qna_num'])
    except Exception as e:
        print('출력오류', e)
    finally:
        conn.commit()
        conn.close()

def qnawritepage(**key):
    conn = connections()
    cursor = conn.cursor()
    sql_update = "update qna set recontent = :recontent where qna_num= :qna_num;"
    try:
        cursor.execute(sql_update,recontent=key['recontent'],qna_num=key['qna_num'])
    except Exception as e:
        print('출력오류', e)
    finally:
        conn.commit()
        conn.close()

