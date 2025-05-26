from django.urls import path
from .views import (
    NewsList,
    ArticleList,
    NewsDetail,
    PostSearch,
    NewsCreate,
    ArticleCreate,
    PostUpdate,
    PostDelete
)

urlpatterns = [
    # Новости
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),

    # Статьи
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/', NewsDetail.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),

    # Поиск (общий)
    path('search/', PostSearch.as_view(), name='post_search'),
]