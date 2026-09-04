from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from posts.models import Comment, Group, Post

from .serializers import CommetSerializer, GroupSerializer, PostSerializer


@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if post.author != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if request.method in ('PUT', 'PATCH'):
        serializer = PostSerializer(
            post,
            data=request.data,
            partial=request.method == 'PATCH'
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def api_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def api_group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    serializer = GroupSerializer(group)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        comments = post.comments.all()
        serializer = CommetSerializer(comments, many=True)
        return Response(serializer.data)
    serializer = CommetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_comment_detail(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id, post=post)
    if request.method == 'GET':
        serializer = CommetSerializer(comment)
        return Response(serializer.data)
    if comment.author != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if request.method in ('PUT', 'PATCH'):
        serializer = CommetSerializer(
            comment,
            data=request.data,
            partial=request.method == 'PATCH'
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
