from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.HomePage.as_view(),name='homepage'),
    path('blog/',views.HomePage.as_view(),name='homepage'),
    path('blog/blogs/',views.BlogListView.as_view(),name='bloglistview'),
    path('blog/<pk>/',views.BlogDetailView.as_view(),name='blogdetailview'),
    path('blog/blogger/<pk>',views.AuthorDetailView.as_view(),name='authordetailview')
]