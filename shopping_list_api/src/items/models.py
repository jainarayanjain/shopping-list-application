from django.db import models
from django.utils.translation import gettext_lazy
from django.conf import settings


class ItemDetail(models.Model):
    """Item Detail"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name=gettext_lazy("user"),
    )
    name = models.CharField(gettext_lazy("name"), max_length=50)
