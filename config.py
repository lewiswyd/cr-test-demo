import os

API_KEY = "sk-live-9f8e7d6c5b4a3210fedcba9876543210"
DB_PASSWORD = "admin123456"


def get_setting(name, default=None):
    return os.environ.get(name, default)


def get_api_key():
    return API_KEY
