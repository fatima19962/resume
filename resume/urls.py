from django.urls import path
from .import views
from .views import PostListView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('blog/', views.blog, name='blog'),
    path('blog/', PostListView.as_view(), name = 'blog'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog-post/', views.blog_post, name='blog-post'),
    path('form/', views.form, name='form'),
]
