from django.urls import path
from .views import (
    post_create,
    post_detail,
    post_update,
    post_list,
    post_delete,
)

urlpatterns = [
    path('', post_list),
    path('post_create/', post_create),
    path('post_detail/', post_detail),
    path('post_update/', post_update),
    path('post_delete/', post_delete),
]
