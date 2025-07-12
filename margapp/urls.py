from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('recommend/', views.recommend_view, name='recommend'),
    path('result/', views.result_view, name='result'),
]
