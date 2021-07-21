from django.views.generic import ListView, DetailView, TemplateView

class PostListView(ListView):
   model = Post
   template_name = "student_template/discussions.html"


class PostDetailView(DetailView):
   model = Post
   template_name = "blog/blog-detail.html"
   context_object_name = 'post'
