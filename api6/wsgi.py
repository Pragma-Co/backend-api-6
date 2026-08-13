"""WSGI config for the API-6 project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api6.settings")

application = get_wsgi_application()
