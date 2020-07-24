# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Contents
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import CreateView
# from .forms import ContentsModelForm


def home(request):
    return render(request, 'landing.html')

# def display(request):
#   return render('index.html', {'obj': models.Contents.objects.all()})

class ContentsList(ListView):
    queryset = Contents.objects.all().order_by('-created_at')
    context_object_name='posts'
    model=Contents
    template_name = 'home.html'
    paginate_by=5

class UserPostListView(ListView):
    model = Contents
    template_name = 'user_contents.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Contents.objects.filter(author=user).order_by('-created_at')


class ContentsDetail(DetailView):
    model = Contents
    template_name = 'contents_detail.html'


class ContentsCreateView(LoginRequiredMixin, CreateView):
    model = Contents
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # form_class = ContentsModelForm
    template_name = 'create.html'
    success_url = '/blogs'

class ContentsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contents
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Contents = self.get_object()
        if self.request.user == Contents.author:
            return True
        return False

class ContentsDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Contents
    template_name = 'post_confirm_delete.html'
    success_url = '/blogs'

    def test_func(self):
        post = self.get_object()
        if self.request.user == Contents.author:
            return True
        return False

def about(request):
    return render(request, 'about.html', {'title': 'About'})

# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
# from django.views.generic import (ListView, DetailView,
#                                   CreateView, UpdateView, DeleteView)
# from .models import Post

# from django.http import HttpResponse


# # Create your views here.




# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     ordering = ['-created_at']
#     paginate_by = 5


# class UserPostListView(ListView):
#     model = Post
#     template_name = 'blog/user_posts.html'
#     context_object_name = 'posts'
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('-created_at')


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
#     model = Post
#     template_name = 'blog/post_confirm_delete.html'
#     success_url = '/blog'

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})