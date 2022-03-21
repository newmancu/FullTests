from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import ChatBlock, ChatUser

# Register your models here.

@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
  pass

@admin.register(ChatBlock)
class ChatBlockAdmin(admin.ModelAdmin):
  pass

admin.site.index_title = _("Some title name")
admin.site.site_header = _("Some header name")
admin.site.site_title = _("Some site title name")