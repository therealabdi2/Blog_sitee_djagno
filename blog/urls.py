from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

urlpatterns = [
    path("", login_required(views.StartingPageView.as_view()), name="starting_page"),
    path("posts", views.AllPostsView.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="posts_detail_page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")

]
