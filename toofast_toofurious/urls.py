from toofast_toofurious.views import *
from django.urls import path
app_name='toofast_toofurious'
urlpatterns=[
    path('cars2/',cars2,name='cars2')
]