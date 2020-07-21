from django.urls import path
from blogs.views import home_view, ContentsList, ContentsDetail, ContentsCreateView

app_name='blogs'
urlpatterns=[
    path('', home_view, name='home'),
    path('blogs/', ContentsList.as_view(), name='Contentslist'),
    path('create', ContentsCreateView.as_view(), name='create'),
    path('<slug:slug>/', ContentsDetail.as_view(), name='Contentsdetail'),
]