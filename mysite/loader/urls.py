from django.urls import path

from .views import RemoteServerCreateView
from . import views

app_name = 'loader'
urlpatterns = [
    # ex: /loader/
    path('', views.index, name='index'),
    path('create', RemoteServerCreateView.as_view(), name='RemoteServerCreateView'),
    path('<int:remote_server_id>/', views.detail, name='detail'),
]
