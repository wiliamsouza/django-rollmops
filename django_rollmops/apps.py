from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _

from .management import create_permissions


class DjangoRollmopsConfig(AppConfig):
    name = 'django_rollmops'
    verbose_name = _('Field level permissions')

    def ready(self):
        post_migrate.connect(
            create_permissions,
            dispatch_uid="django_rollmops.management.create_permissions"
        )
