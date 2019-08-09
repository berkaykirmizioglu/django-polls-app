from django.db import models


# Create your models here.
class RemoteServer(models.Model):
    remote_server_ip = models.CharField('Remote Server Ip', max_length=15)
    port = models.CharField('Port', max_length=5)
    is_active = models.BooleanField('Activity', default=False)
