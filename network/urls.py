
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("allpost", views.allpost, name="allpost"),
    path("like/<str:lid>", views.like, name="like"),
    path("new", views.new, name="new"),
    path("profile/<username>", views.profile, name="profile"),
    path('follow/<str:target>', views.follow, name='follow'),
    path('unfollow/<str:target>', views.unfollow, name='unfollow'),
    path('followpost', views.followpost, name='followpost'),
    path("edit/<str:post_id>", views.edit, name="edit"),

]
