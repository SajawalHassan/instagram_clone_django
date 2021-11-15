from django.urls import path
from .views import HomeView, CreatePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create_post/', CreatePostView.as_view(), name="create_post"),
]
