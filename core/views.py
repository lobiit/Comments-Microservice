from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Comment
from core.serializers import CommentSerializer


class PostCommentAPIView(APIView):
    def get(self, _, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# Create your views here.
class CommentAPIView(APIView):
    # def get(self, request):
    #     posts = Comment.objects.all()
    #     serializer = CommentSerializer(posts, many=True)
    #
    #     return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
