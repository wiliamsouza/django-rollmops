from django.apps import apps
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django_rollmops.management import create_permissions


def test_create_permissions_models_field(db):
    content_type = ContentType.objects.get_by_natural_key(
        'tests',
        'defaultpermission'
    )

    # NOTE: When django.contrib.auth is listed in your INSTALLED_APPS setting,
    # it will ensure that three default permissions – add, change and delete –
    # are created for each Django model defined in one of your installed
    # applications.
    assert Permission.objects.filter(content_type=content_type).count() == 3

    app_config = apps.get_app_config('tests')
    create_permissions(app_config, verbosity=0)

    assert Permission.objects.filter(content_type=content_type).count() == 9


def test_create_permission_models_custom_field(db):
    content_type = ContentType.objects.get_by_natural_key(
        'tests',
        'custompermission'
    )

    assert Permission.objects.filter(content_type=content_type).count() == 4

    app_config = apps.get_app_config('tests')
    create_permissions(app_config, verbosity=0)

    assert Permission.objects.filter(content_type=content_type).count() == 10


def test_create_permissions_models_choice_field(db):
    content_type = ContentType.objects.get_by_natural_key(
        'tests',
        'choicepermission'
    )

    assert Permission.objects.filter(content_type=content_type).count() == 3

    app_config = apps.get_app_config('tests')
    create_permissions(app_config, verbosity=0)

    assert Permission.objects.filter(content_type=content_type).count() == 15


def test_create_permission_models_empty_field(db):
    content_type = ContentType.objects.get_by_natural_key(
        'tests',
        'emptypermission'
    )

    assert Permission.objects.filter(content_type=content_type).count() == 0

    app_config = apps.get_app_config('tests')
    create_permissions(app_config, verbosity=0)

    assert Permission.objects.filter(content_type=content_type).count() == 0
