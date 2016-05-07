#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render
# Create your views here.
import sys
from django.http import HttpResponse
from intro.models import Character
from django.core.context_processors import csrf
from django import forms
# ------------------------get coordinate code-------------------------------------------------------------
import requests
import json
import random
# ------------------------get coordinate code-------------------------------------------------------------

reload(sys)
sys.setdefaultencoding('utf-8')

def first_page(request):
    return HttpResponse("<p>西餐</p>")

# ------------------------get coordinate code-------------------------------------------------------------
class FootPrint():
    def __init__(self,data):
        self.key = 'q5mTrTGzCSVq5QmGpI9y18Bo'
        self.url = 'http://api.map.baidu.com/geocoder/v2/?output=json&ak=%s&address=' % (self.key)
        self.color = None
#        self.data = ['郑州 陕西西安 武汉 苏州 郑州 北京',]
        self.data = data

#        self.region = config.get('region','china')
        self.alldata = {}
        self.linedata = []
        self.pointdata = []
        self.cache = {}
    def processData(self):
        for route in self.data:
            tmp = route.split()
            for t in tmp:
                self.cache[t] = self.getValue()
                if t not in self.alldata:
                    self.getPoint(t)

            for i in range(len(tmp)-1):
                val = self.getValue()
                self.linedata.append([{'name':tmp[i]},{"name":tmp[i+1],'value':self.cache[tmp[i+1]]}])
        for name in self.alldata:
            self.pointdata.append({'name':name,'value':self.cache[name]})

    def getPoint(self,name):
        url = self.url+name
        try:
            r = requests.get(url)
            res = r.json()
            if res.get('result',None):
                loc = res['result']['location']
                self.alldata[name] = [loc['lng'],loc['lat']]
        except:
            print '获取不到%s的经纬度信息'%(name)

    def getValue(self):
        if self.color:
            return random.randint(0,100)
        else:
            return 1
    def start(self):
        self.processData()

# ------------------------get coordinate code-------------------------------------------------------------

def introduction_template(request):
    context = {}
    context['label'] = "The footprint app can let you to show you footprint on the map, it's very interesting ~"
    return render(request, 'introduction.html', context)

def form(request):
    return render(request, 'form.html')

def handle_form(request):
    request.encoding='utf-8'
#    foot = ['郑州 南阳']
    foot = []

    data = request.GET['title']
    foot.append(data)
    F = FootPrint(foot)
    F.start()
    context = {}
    context['label_0'] = "陕西西安，武汉，苏州，郑州"
    context['label_1'] = "上海"
    context['region'] = "china"
    context['alldata'] = json.dumps(F.alldata)
    print context['alldata']
    context['linedata'] = json.dumps(F.linedata)
    context['pointdata'] = json.dumps(F.pointdata)
    return render(request, 'footprint.html', context)



















