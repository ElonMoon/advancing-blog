from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    queryset = Post.objects.all()
    context = {'posts': queryset}
    return render(request, 'index.html', context)


def post_create(request):
    return HttpResponse('<p>포스트 생성입니다</p>')


def post_detail(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    context = {
        'post': instance,
    }
    return render(request, 'post_detail.html', context)


def post_update(request):
    return HttpResponse('<p>포스트 수정입니다</p>')


def post_delete(request):
    return HttpResponse('<p>포스트 삭제입니다</p>')
