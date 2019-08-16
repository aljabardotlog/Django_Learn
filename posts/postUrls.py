from django.urls import path
from posts import views as post_view

urlpatterns = [
    path('', post_view.post_list),
    path('post_create/', post_view.post_create),
    path('post_detail/', post_view.post_detail),
    path('post_update/', post_view.post_update),
    path('post_delete/', post_view.post_delete),
]
