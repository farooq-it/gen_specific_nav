from fast_furious.views import *
from django.urls import path
app_name='fast_furious'
urlpatterns=[
    path('cars1/',cars1,name='cars1')
]