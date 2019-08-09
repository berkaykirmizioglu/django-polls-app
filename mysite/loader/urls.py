from django.urls import path

from . import views

app_name = 'loader'
urlpatterns = [
    # ex: /loader/
    path('', views.index, name='index'),
]
