from django.views.generic import ListView, CreateView
from .models import Post
from .forms import CreatePostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    # fields = '__all__'
    form_class = CreatePostForm
