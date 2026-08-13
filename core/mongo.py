"""Shared MongoDB client for the whole project.

Django has no native MongoDB backend, so the document database is
accessed directly through pymongo. Import get_mongo_db() anywhere a
MongoDB collection is needed.
"""

from urllib.parse import quote_plus

from django.conf import settings
from pymongo import MongoClient

_client = None


def get_mongo_client() -> MongoClient:
    global _client
    if _client is None:
        # The URI is assembled here rather than stored in settings so the
        # password never shows up in Django's debug-page settings dump.
        uri = "mongodb://{user}:{password}@{host}:{port}/".format(
            user=quote_plus(settings.MONGO_USER),
            password=quote_plus(settings.MONGO_PASSWORD),
            host=settings.MONGO_HOST,
            port=settings.MONGO_PORT,
        )
        _client = MongoClient(uri, serverSelectionTimeoutMS=3000)
    return _client


def get_mongo_db():
    return get_mongo_client()[settings.MONGO_DB_NAME]
