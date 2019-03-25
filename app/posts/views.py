from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse('<p>포스트 리스트입니다</p>')


def post_create(request):
    return HttpResponse('<p>포스트 생성입니다</p>')


def post_detail(request):
    return HttpResponse('<p>포스트 하나입니다</p>')


def post_update(request):
    return HttpResponse('<p>포스트 수정입니다</p>')


def post_delete(request):
    return HttpResponse('<p>포스트 삭제입니다</p>')
