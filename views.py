# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "surveyApp/index.html")

def submit(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
    else:
        print request.method
    return redirect("/survey/result/")

def result(request):
    context = {
        "name":request.session["name"],
        "location":request.session["location"],
        "language":request.session["language"],
        "comment":request.session["comment"]
        }
    return render(request, "surveyApp/result.html", context)

def back(request):
    return redirect("/survey/")