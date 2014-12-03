"""
Django settings for mashup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from ConfigParser import RawConfigParser
import os
# ex /jiracharts
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# ex /jiracharts/jiracharts
PROJECT_DIR = os.path.dirname(__file__)
# ex /
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# ConfigParser
config = RawConfigParser()
# CONF_DIR/conf/
config.read('{0}/conf/apimashupconf.ini'.format(ROOT_DIR))
SECRET_KEY = config.get('settings','secret_key')

#twilio
TWILIO_ACCOUNT_SID = config.get('twilio','account_sid')
TWILIO_AUTH_TOKEN = config.get('twilio','auth_token')
TWILIO_FROM_PHONE_NUMBER = config.get('twilio','from_phone_number')

#mashape
X_MASHAPE_KEY = config.get('mashape','key')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'yodasms/templates')]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mashup.urls'

WSGI_APPLICATION = 'mashup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)