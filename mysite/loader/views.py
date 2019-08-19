from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .models import RemoteServer


def index(request):
    return render(request, 'loader/index.html')


def detail(request, remote_server_id):
    remote_server = RemoteServer.objects.get(pk=remote_server_id)
    context = {'remote_server': remote_server}
    return render(request, 'loader/remoteServerDetails.html', context)


class RemoteServerCreateView(CreateView):
    model = RemoteServer
    template_name = 'loader/addRemoteServer.html'
    fields = ('remote_server_ip', 'port', 'is_active')

