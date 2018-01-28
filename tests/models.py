from django.db import models

STATUS_CHOICES = (
    ('created', 'Created'),
    ('published', 'Published'),
)


class DefaultPermission(models.Model):
    name = models.CharField(max_length=255)


class CustomPermission(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        permissions = (
            (
                'see_custompermission__name',
                'Can see custompermission name field'
            ),
        )


class ChoicePermission(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=64,
        default='created',
        choices=STATUS_CHOICES
    )


class EmptyPermission(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # NOTE: You may customize this list, for example, by setting this to
        # an empty list if your app doesn’t require any of the default
        # permissions.
        default_permissions = []
