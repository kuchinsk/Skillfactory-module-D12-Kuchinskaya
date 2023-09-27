"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path, os
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@)51a42kpyan%xib=n2e#sd_+5z8#3tyf1nh6#!ou8x0b2u1)!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'news',
    'sign',
    'django_filters',

    "django_apscheduler",
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# LOGIN_URL = '/news/'
LOGIN_URL = '/sign/login/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {'signup': 'sign.forms.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'kuchinsk93'
EMAIL_HOST_PASSWORD = 'hhgpvluhmjsrdpnb'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'kuchinsk93@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 30,
    }
}

ADMINS = [("Anna", "kuchinsk93@yandex.ru")]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'time_level_msg': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'time_level_msg_path': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'time_level_msg_path_stack': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'time_level_modul_msg': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console_debag': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'time_level_msg'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'time_level_msg_path'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'time_level_msg_path_stack'
        },
        'general_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'time_level_modul_msg'
        },
        'errors_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'time_level_msg_path_stack'
        },
        'security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'time_level_modul_msg'
        },
        'mail_error': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'time_level_msg_path'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_debag', 'console_warning', 'console_error', 'general_info'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors_error', 'mail_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors_error', 'mail_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': True,
        },
    }
}