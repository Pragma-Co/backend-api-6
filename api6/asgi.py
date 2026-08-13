"""ASGI config for the API-6 project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api6.settings")

application = get_asgi_application()
