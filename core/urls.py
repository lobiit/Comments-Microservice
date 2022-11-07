from django.contrib import admin
from django.urls import path
from .views import CommentAPIView, PostCommentAPIView

urlpatterns = [
    path('comments', CommentAPIView.as_view()),
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view()),
]
