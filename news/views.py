from django.views.generic import ListView, DetailView
from .models import Post
from .models import Comment
from .models import PostCategory
from .models import Category
from .models import Author

class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    ordering = '-created_at'
    context_object_name = 'news_list'

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['comments'] = Comment.objects.filter(post=self.object)
        return context