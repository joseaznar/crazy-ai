from django.conf.urls import url
from django.contrib import admin
from .views import ListTopReTweets

urlpatterns = [
    #url(r'^(?P<query>[\w]+)/$', ListTweets.as_view()),
    url(r'^(?P<query>.+)/$', ListTopReTweets.as_view()),
    #url(r'^$', ListTweets.as_view()),
]