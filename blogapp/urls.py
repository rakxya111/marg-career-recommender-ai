from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post-list/', views.PostListView.as_view(), name='post-list'),
    path('post-by-tag/<int:tag_id>/',views.PostByTagView.as_view(), name='post-by-tag'),
    
]