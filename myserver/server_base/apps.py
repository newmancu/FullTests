from django.apps import AppConfig


class ServerBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server_base'
