from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page_url"),
    path("posts/", views.posts, name="posts_url"),
    path("posts/<str:slug>", views.the_post, name="post_url")
]