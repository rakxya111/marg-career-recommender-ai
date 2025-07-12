from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from blogapp.models import Post
from django.views.generic import ListView,TemplateView,DetailView,View
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q



# Home View
def home_view(request):
    return render(request, 'marg/base.html')

class PostListView(ListView):
    model = Post
    template_name = 'marg/Blog/BlogList/bloglist.html'
    context_object_name = "posts"
    
    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False, status='active'
        ).order_by('-published_at')

class PostByTagView(ListView):
    model = Post
    template_name = 'marg/Blog/BlogList/bloglist.html'
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status='active',
            tag__id=self.kwargs['tag_id'],
        ).order_by['-published_at']
        return query

class PostDetailView(DetailView):
    pass


