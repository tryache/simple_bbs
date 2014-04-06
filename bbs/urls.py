from django.conf.urls import patterns, include, url
from django.contrib import admin
from bbs import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^posts/?', include('posts.urls', namespace="posts")),
    url(r'^login/?', views.LoginView.as_view(), name="login"),
    url(r'^logout/?', views.LogoutView.as_view(), name="logout"),
    url(r'^register/?', views.RegisterView.as_view(), name="register"),
    url(r'^', views.IndexView.as_view(), name="index"),
)
