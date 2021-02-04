# coding: utf-8

from pathlib import Path
import environ


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR.joinpath(".env").resolve()

env = environ.Env()

if Path.exists(ENV_FILE):
    env.read_env(env.str('ENV_PATH', str(ENV_FILE)))
else:
    environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'podcasts.apps.PodcastsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mainconfig.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mainconfig.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env("DATABASE_HOST"),
        'PORT': env("DATABASE_PORT"),
        'USER': env("DATABASE_USERNAME"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'NAME': env("DATABASE_NAME"),
    }
}

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

LANGUAGE_CODE = env('LANGUAGE_CODE')
TIME_ZONE = env('TIME_ZONE')
USE_I18N = env.bool('USE_I18N')
USE_L10N = env.bool('USE_L10N')
USE_TZ = env.bool('USE_TZ')

STATIC_URL = '/assets/'
