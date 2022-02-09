from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_home(request):
    content = '<h1>여기는 홈 화면입니다. </h1>' # HTML 태크를 리턴
    return HttpResponse(content)