from django.conf.urls import url
from . import views

urlpatterns = [
    path(r'^templates/', views.index_template, name='index_template'),
]
