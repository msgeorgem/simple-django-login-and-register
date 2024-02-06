import os
from os.path import dirname, abspath, join




IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *

bootstrap5 = {
    'include_jquery':True,     
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Application apps
    'main',
    'accounts',

    # Vendor apps
    'bootstrap4',
]


