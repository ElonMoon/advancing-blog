from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='타이틀', max_length=128)
    content = models.TextField(verbose_name='내용')
    timestamp = models.DateTimeField(verbose_name='생성일자', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='수정일자', auto_now=True)

    def __str__(self):
        return self.title
