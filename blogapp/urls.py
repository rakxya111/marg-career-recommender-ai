from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
]