from django.contrib import admin
from django.conf.urls import url,include
from django.http import HttpResponse
from movie import urls as urls2
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/',include(urls2)),
]
# from django.conf.urls import url
# urlpatterns = [
# url('',views.homepageview,name='home')