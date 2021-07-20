from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment

class PostListView(ListView):
    model = Post
    template_name = "forum/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog-detail.html"
    context_object_name = 'post'
