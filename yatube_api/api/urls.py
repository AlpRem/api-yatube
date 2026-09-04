from django.urls import path
from rest_framework.authtoken import views

from .views import (api_comment_detail, api_comments, api_group_detail,
                    api_groups, api_post_detail, api_posts)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/posts/', api_posts),
    path('v1/posts/<int:post_id>/', api_post_detail),
    path('v1/groups/', api_groups),
    path('v1/groups/<int:group_id>/', api_group_detail),
    path('v1/posts/<int:post_id>/comments/', api_comments),
    path(
        'v1/posts/<int:post_id>/comments/<int:comment_id>/',
        api_comment_detail
    ),
]
