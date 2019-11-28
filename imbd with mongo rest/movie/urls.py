from django.conf.urls import url
from django.urls import path
from .views import greet,get_director,get_popular,get_top,get_least,get_popu
    #,get_one_article,get_all_articles
urlpatterns=[
    path('hello/', greet),
    path('first/', get_director),
    path('all/', get_popular),
    path('top/',get_top),
    path('least/',get_least),
    path('dir/',get_popu),


] 
