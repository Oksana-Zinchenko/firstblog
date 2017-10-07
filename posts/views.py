from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from posts.models import Post


def index(request):
    return render(request, 'base.html', {'posts': Post.objects.all()})

class PostList(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginator_class = None


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'