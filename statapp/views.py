# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
import pandas as pd

def hello(request):
    return HttpResponse('Hello World')
# Create your views here.
def home(request):
    pd.set_option('display.max_columns', 50)
    pd.set_option('display.width', 200)
    template=get_template('home.html')
    if 'd' in request.GET:
        df = pd.read_csv(request.GET['d'], encoding='gbk').head(5)
        request.session['path']=request.GET['d']
    else:
        df=pd.DataFrame()
    col=pd.DataFrame(df.columns).T
    html=template.render(locals())
    return HttpResponse(html)

def ttest(request):
    path = request.session['path']
    template=get_template('ttest.html')
    df = pd.read_csv(path, encoding='gbk').head(5)
    col=pd.Series(df.columns)
    if 'column' in request.GET:
        column=request.GET['column']
    if 'outcome' in request.GET:
        outcome=request.GET['outcome']
    html=template.render(locals())
    return HttpResponse(html)

def data(request):
    pd.set_option('display.max_columns',50)
    pd.set_option('display.width', 8000)
    #df=pd.read_csv(request.GET['d'],encoding='gbk')
    #df1=df.iloc[:,0]
    col=pd.Series(df.columns)
    return render_to_response('data.html',{'df':df,'col':col})

def time(request):
    template=get_template('time.html')
    html=template.render(locals())
    return HttpResponse(html)

def asktime(request):
    print 'hello'
    q=request.GET['name']
    print q
    ans=q+'，'+'哈哈哈'
    return HttpResponse(ans)

def ttest_result(request):
    column=request.GET['column']
    outcome=request.GET['outcome']
    html=column+outcome
    return HttpResponse(html)

