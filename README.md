django-rollmops
=


[![Build Status](https://travis-ci.org/wiliamsouza/django-rollmops.svg)](https://travis-ci.org/wiliamsouza/django-rollmops)
[![Coverage Status](https://coveralls.io/repos/wiliamsouza/django-rollmops/badge.svg?branch=master&service=github)](https://coveralls.io/github/wiliamsouza/django-rollmops?branch=master)

Django rollmops is a field level permmisions for your modules.

When `django_rollmops` is listed in your `INSTALLED_APPS` setting,
it will ensure that three default permissions – add, change and delete –
are created for each Django model *fields* and fields *choices* defined in one
of your installed applications.
