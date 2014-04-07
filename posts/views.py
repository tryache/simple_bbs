from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from posts.models import Post, Reply


class IndexView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "posts/posts.html", {'posts': posts, 'title': 'posts', 'user_id': self.request.user})


class DetailView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        replys = Reply.objects.filter(post=post_id)
        return render(request, "posts/detail.html", {'post': post, 'replys': replys, 'user_id': self.request.user, 'title': post.title})

    # def post(self, request):
    #     re
    # def update(self, request):
    #
    # def delete(self, request, poll_id):


class ResultsView(View):
    model = Post
    template_name = 'polls/results.html'