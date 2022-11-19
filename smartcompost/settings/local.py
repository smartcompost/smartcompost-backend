from .base import *

SECRET_KEY = "secret_key"
ALLOWED_HOSTS = ["*"]

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "smartcompost"),
        "USER": env("POSTGRES_USER", "smartcompost"),
        "PASSWORD": env("POSTGRES_PASSWORD", "smartcompost"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}
