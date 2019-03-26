from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


def post_list(request):
    queryset = Post.objects.all()
    context = {'posts': queryset}
    return render(request, 'index.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)


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
