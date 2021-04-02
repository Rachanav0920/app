from django.shortcuts import render
from django.http import HttpResponse
import os

file_path=os.path.abspath(__file__)
pro_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro_dir_path)

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to index page....</h1>")

def rend_demo(request):
    return render(request,"sample.html")     