from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class ChatUser(models.Model):

  user_name = models.CharField(
    _("UserName"),
    help_text=_('User name field'),
    max_length=40
  )

  reg_date = models.DateTimeField(
    _('Registration Date'),
    help_text=_('User name field'),
    auto_now=True
  )


  class Meta:
    verbose_name = _('ChatUser')
    verbose_name_plural = _('ChatUsers')


class ChatBlock(models.Model):
  
  users = models.ManyToManyField(
    f"ChatUser",
    help_text=_('User name field'),
    verbose_name=_('ChatUser'),
  )
  
  chat_name = models.CharField(
    _('ChatName'),
    help_text=_('User name field'),
    max_length=128
  )

  def __repr__(self) -> str:
    return f"{self.pk} - {self.chat_name}"

  def __str__(self) -> str:
    return self.__repr__()


  class Meta:
    verbose_name = _('ChatBlock')
    verbose_name_plural = _('ChatBlocks')