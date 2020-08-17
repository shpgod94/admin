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

def qnawrite(**key):
    conn = connections()
    cursor = conn.cursor()
    sql_update = "update qna set recontent = :recon ,qtitle= :qtitle where qna_num= :qna_num"
    try:
        cursor.execute(sql_update, recon=key['recontent'], qtitle=key['qtitle'], qna_num=key['qna_num'])
    except Exception as e:
        print('출력오류', e)
    finally:
        conn.commit()
        conn.close()

def selzz():
    conn = connections()
    cursor = conn.cursor()
    sql_sellist = "select p.MERCHANT_UID, p.PRODUCT_NUM, p.BUYER_NUM, p.imp, p.PAID_AMOUNT, p.PAID_DATE, p.PAID_COUNT, u.user_id from paylist p, user_info u where p.buyer_num = u.user_num order by p.PAID_DATE desc"
    try:
        cursor.execute(sql_sellist)
    except Exception as e:
        print('출력오류', e)
    finally:
        sel = cursor.fetchall()
        cursor.close()
        conn.close()
    return sel

def banuser():
    conn = connections()
    cursor = conn.cursor()
    sql_banuserlist = "select * from report_user order by report_num"
    try:
        cursor.execute(sql_banuserlist)
    except Exception as e:
        print('출력오류', e)
    finally:
        ban = cursor.fetchall()
        cursor.close()
        conn.close()
    return ban

def banuser2():
    conn = connections()
    cursor = conn.cursor()
    sql_banboardlist = "select * from report_board order by report_board_num"
    try:
        cursor.execute(sql_banboardlist)
    except Exception as e:
        print('출력오류', e)
    finally:
        ban = cursor.fetchall()
        cursor.close()
        conn.close()
    return ban

def banuser3():
    conn = connections()
    cursor = conn.cursor()
    sql_bancommentlist = "select * from report_comment order by report_comment_num"
    try:
        cursor.execute(sql_bancommentlist)
    except Exception as e:
        print('출력오류', e)
    finally:
        ban = cursor.fetchall()
        cursor.close()
        conn.close()
    return ban