from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request,'myHome/index.html',{})

def content(request):
  return render(request,'myHome/content.html',{})