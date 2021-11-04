from django.urls import path, include
# from .views import
from . import views

app_name = 'post'
urlpatterns = [
    path('create', views.CommentCreateAPIView.as_view(), name='create'),
    path('list', views.CommentListAPIView.as_view(), name='list'),
    path('delete/<pk>', views.CommentDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', views.CommentUpdateAPIView.as_view(), name='update')
]
