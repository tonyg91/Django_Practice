from typing import final
from django.shortcuts import render
from django.http import JsonResponse
from routes.models import Todo
from django.core.serializers import serialize
from json import loads
from routes.models import Journals
from routes.models import Supply


def HelloWorld(request):
    return JsonResponse({"hello": "wolrd"})

def index(request):
    all = Todo.objects.all()
    alljson= serialize("json", all)
    final = loads(alljson)
    return JsonResponse(final, safe=False)

def jindex(request):
    all = Journals.objects.all()
    alljson = serialize("json", all)
    final = loads(alljson)
    return JsonResponse(final, safe=False)

def sindex(request):
    all = Supply.objects.all()
    alljson = serialize("json", all)
    final = loads(alljson)
    return JsonResponse(final, safe=False)