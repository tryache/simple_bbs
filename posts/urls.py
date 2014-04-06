from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^new/$', views.NewPostView.as_view(), name='index'),
    url(r'^(?P<post_id>\d+)/?$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<post_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
