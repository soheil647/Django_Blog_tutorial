from django.urls import path, include
from . import views
from user import views as user_view
from .views import PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('about/', views.about_page, name='blog-about'),
]
