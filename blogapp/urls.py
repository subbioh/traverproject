from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>',views.detail, name="detail"),
    path('new/', views.blogpost, name='new'),
    path('create',views.create, name="create"),
    #path('newblog/', views.blogpost, name="newblog"),
]