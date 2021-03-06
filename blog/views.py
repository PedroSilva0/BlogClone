from django.shortcuts import redirect, render, get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post,Comment
from blog.forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


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


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    template_name = 'post_draft_list.html'

    model = Post

    def get_queryset(self):
        result = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        return result

############################################
############################################

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
    



@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk = post.pk)
    else:
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk = comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk = post_pk)

