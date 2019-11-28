from django.shortcuts import render
from django.http import HttpResponse
#from .models import Article
from django.http import JsonResponse
from pymongo import MongoClient
from datetime import datetime
from pprint import pprint
from rest_framework.decorators import api_view
client = MongoClient()
db = client['moviestest']

def greet(request):
    return HttpResponse("<h1>Hello PNV<h1>")
@api_view(['GET'])
def get_director(request):
    collection = db['students']
    cursor = collection.aggregate([{"$group" : {"_id":"$director","count":{"$sum":1}}}])
    data,l = list(cursor),[]
    for i in data:
        for j in i.items():
            ab = isinstance(j[1], int)
            if ab == True:
                l.append(j[1])
        p=max(l)
        if i['count']==p:
            a=i
            b=a["_id"]
    data12 = collection.find_one({"director":b},{"_id": 0})
    return JsonResponse(data12,safe=False)

@api_view(['GET'])
def get_popular(request):
        collection = db['students']
        cursor = collection.aggregate([{"$group": {"_id": "$99popularity", "count": {"$sum": 1}}}])
        data, l = list(cursor), []
        for i in data:
            j1=i["_id"]
            l.append(j1)
        p=max(l)
        data12 = collection.find_one({"99popularity": p}, {"_id": 0})
        return JsonResponse(data12, safe=False)
@api_view(['GET'])
def get_top(request):
    collection = db['students']
    cursor = collection.aggregate([{"$group" : {"_id": "$imdb_score", "count": {"$sum": 1}}}])
    data,l,m,q1=list(cursor),[],[],[]
    for i in data:
        j1 = i["_id"]
        l.append(j1)
    for e in range(1,6):
             w=max(l,key=lambda x:x)
             m.append(w)
             l.remove(w)
    for m1 in m:
           data12 = collection.find_one({"imdb_score": m1}, {"_id": 0})
           q1.append(data12)
    return JsonResponse(q1, safe=False)
@api_view(['GET'])
def get_least(request):
    collection = db['students']
    cursor = collection.aggregate([{"$group" : {"_id": "$imdb_score", "count": {"$sum": 1}}}])
    data,l,m,q1=list(cursor),[],[],[]
    for i in data:
        j1 = i["_id"]
        l.append(j1)
    w=min(l,key=lambda x:x)
    data12 = collection.find_one({"imdb_score": w}, {"_id": 0})
    return JsonResponse(data12, safe=False)
@api_view(['GET'])
def get_popu(request):
        collection = db['students']
        cursor = collection.aggregate([{"$group": {"_id": "$99popularity", "count": {"$sum": 1}}}])
        data, l = list(cursor), []
        for i in data:
            j1=i["_id"]
            l.append(j1)
        p=max(l)
        data12 = collection.find_one({"99popularity":p},{"_id": 0})
        return JsonResponse(data12, safe=False)
