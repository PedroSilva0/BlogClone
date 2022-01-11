from django.conf.urls import url

from blog.views import AboutView, DraftListView, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/$', DraftListView.as_view(), name='post_draft_list'),
]