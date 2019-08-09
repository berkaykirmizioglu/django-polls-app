from django.contrib import admin
from .models import RemoteServer

# Register your models here.


class RemoteServerAdmin(admin.ModelAdmin):
    list_display = ('remote_server_ip', 'port', 'is_active')


admin.site.register(RemoteServer, RemoteServerAdmin)

