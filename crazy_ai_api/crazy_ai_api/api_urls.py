
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
url(r'^tweets/', include("modules.twitter.urls")),
url(r'^watson/', include("modules.watson.urls")),
]