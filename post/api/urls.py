from django.urls import path, include
# from .views import
from . import views

app_name = 'post'
urlpatterns = [
    path('list', views.PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', views.PostDetailAPIView.as_view(), name='detail'),
    path('delete/<slug>', views.PostDeleteAPIView.as_view(), name='delete'),
    path('update/<slug>', views.PostUpdateAPIView.as_view(), name='update'),
    path('create/', views.PostCreateAPIView.as_view(), name='create')
]
