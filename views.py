# news/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Post, Author, Comment
from .forms import PostForm
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    ordering = '-created_at'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(post_type='NW')  # Только новости


class ArticleList(ListView):
    model = Post
    template_name = 'news/article_list.html'
    ordering = '-created_at'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(post_type='AR')  # Только статьи


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['comments'] = Comment.objects.filter(post=self.object)
        return context


class PostSearch(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search_results'
    paginate_by = 10
    ordering = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['filterset'] = self.filterset
        return context


class NewsCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NW'
        author, created = Author.objects.get_or_create(user=self.request.user)
        post.author = author
        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'
        author, created = Author.objects.get_or_create(user=self.request.user)
        post.author = author
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def get_success_url(self):
        if self.object.post_type == 'NW':
            return reverse_lazy('news_list')
        else:
            return reverse_lazy('news_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'news/post_delete.html'

    def get_success_url(self):
        if self.object.post_type == 'NW':
            return reverse_lazy('news_list')
        else:
            return reverse_lazy('news_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)