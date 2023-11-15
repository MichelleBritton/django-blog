from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # The first slug is a path converter which converts this text into a slug field, it tells django to match any slug string,
    #  the second slug is a keyword name. The slug keyword name matches the 'slug parameter in the get method of the PostDetail 
    # class in the blog/views.py file, that's how we link them together
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]