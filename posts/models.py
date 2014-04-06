from django.db import models
import django.contrib.auth.models
# Create your models here.


class Post(models.Model):
    title = models.TextField("标题")
    content = models.TextField("内容")
    author = models.ForeignKey(django.contrib.auth.models.User)
    post_date = models.DateTimeField("发布日期", auto_now=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(Post)
    title = models.TextField("标题")
    content = models.TextField("内容")
    author = models.ForeignKey(django.contrib.auth.models.User)
    post_date = models.DateTimeField("发布日期", auto_now=True)

    def __str__(self):
        return self.title

