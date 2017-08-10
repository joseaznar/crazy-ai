from django.conf.urls import url
from django.contrib import admin
from .views import ProcessTweets

urlpatterns = [
    url(r'^(?P<query>[\w]+)/$', ProcessTweets.as_view()),
]