from .base import *

DEBUG = False
ALLOWED_HOSTS += [
   'learningdeck.herokuapp.com',
]

MIDDLEWARE += [
   'whitenoise.middleware.WhiteNoiseMiddleware',
]

WSGI_APPLICATION = 'student_management_system.wsgi.prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)