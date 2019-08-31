from django.conf.urls import url
from . import views
#index -> show hello
#play -> show 畫面
#returnlist ->web api
urlpatterns=[
    url(r'^$',views.index , name='index'),
    #url(r'^/play/$',views.playmusic, name='playmusic'),
    #url(r'^/returnlist/(?P[0-9]+)$',views.returnlist,name='returnlist'),
]

