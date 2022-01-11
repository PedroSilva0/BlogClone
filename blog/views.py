from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post,Comment
from blog.forms import PostForm
from django.urls import reverse_lazy


# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post
    #template_name = "TEMPLATE_NAME"

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        

class PostDetailView(DetailView):
    model = Post
    #template_name = "TEMPLATE_NAME"


class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm

    model = Post
    #template_name = "TEMPLATE_NAME"


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
    #template_name = "TEMPLATE_NAME"


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    #template_name = "TEMPLATE_NAME'


class DraftListView(ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    #template_name = "TEMPLATE_NAME"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
     








