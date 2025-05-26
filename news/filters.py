import django_filters
from django import forms
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Название содержит'
    )

    author__user__username = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Имя автора'
    )

    created_after = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gt',
        label='Не ранее',
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = []