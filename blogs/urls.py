from django.urls import path
from blogs.views import home, UserPostListView, ContentsList, ContentsDetail, ContentsCreateView,ContentsUpdateView,ContentsDeleteView
from .import views

app_name='blogs'
urlpatterns=[
    path('',ContentsList.as_view(), name='home'),
    # path('', home_view, name='home'),
    # path('blogs/', ContentsList.as_view(), name='Contentslist'),
    path('blogs/new/', ContentsCreateView.as_view(), name='create'),
    path('blogs/<int:pk>/', ContentsDetail.as_view(), name='Contentsdetail'),
    path('blogs/<int:pk>/update/', ContentsUpdateView.as_view(), name='ContentsUpdateView'),
    path('blogs/<int:pk>/delete/', ContentsDeleteView.as_view(), name='ContentsDeleteView'),
    path('about/', views.about, name='about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
]

#  path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),