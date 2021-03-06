from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    ## add your url here
    url(r'^posts/search/(?P<term>.*)$','blog.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit','blog.views.edit_comment')

)
