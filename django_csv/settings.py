"""
Django settings for django_csv project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xfrfpyj)bw*048d6(v*w@=ok!2ms!gw_b%ijuv66m38rt^ul_t'

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
    'app_csv',
    "csp",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = 'django_csv.urls'

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

WSGI_APPLICATION = 'django_csv.wsgi.application'


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


CSP_INCLUDE_NONCE_IN = ['script-src' , 'nonce']
CSP_DEFAULT_SRC = ("'self'",)


CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "fonts.googleapis.com",
    "use.fontawesome.com",
    "ajax.googleapis.com",
    "google.com",
    "googletagmanager.com",
    "https://www.googletagmanager.com",
    "https://www.googletagmanager.com",
    "www.googletagmanager.com",
    "https://cdn.jsdelivr.net",)


CSP_SCRIPT_SRC = (
    "'self'",
    # "'unsafe-inline'",
    # "'unsafe-eval'",
    "gstatic.com",
    "google.com",
    "googleadservices.com",
    "script.hotjar.com",
    "maps.googleapis.com",
    "googletagmanager.com",
    "google-analytics.com",
    "https://analytics.google.com")


CSP_SCRIPT_SRC = (
    "'self'",
    "https://www.googletagmanager.com",
    'https://cdn.cookielaw.org',
    'www.trialx.com',
    'https:'
    "https://cdn.jsdelivr.net",
)


CSP_CONNECT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "onetrust.com",
    "https://geolocation.onetrust.com",
    "cdn.cookielaw.org",)

CSP_FRAME_SRC = (
    "'self'",
    "google.com",
    "https://www.google.co.id",
    "https://www.google.com.pe",
    "https://www.google.co.ze",)

CSP_FONT_SRC = (
    "'self'",
    'data:',
    "use.fontawesome.com",
    "fonts.gstatic.com",
    "fonts.googleapis.com",
    "https://www.google.com",
    "fonts.cdnfonts.com",
    "maps.googleapis.com",
    "https://vimeo.com",
    "https://www.googleoptimize.com",
    'fonts.gstatic.com',
    'cdnjs.cloudflare.com',
    'fonts.gstatic.com',
    '*.cloudfront.net',
    'https://players.brightcove.net',
    'www.google-analytics.com',
    "*.doubleclick.net",
    "*.hotjar.com",
)

CSP_IMG_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    'data:',
    "google.com",
    "maps.gstatic.com",
    "googleadservices.com",
    "google.co.in",
    "googleads.g.doubleclick.net",
    "ajax.googleapis.com",
    "google-analytics.com",
    "googletagmanager.com",
    "https://www.google.com",
    "maps.googleapis.com",
    "purecatamphetamine.github.io",
    "cdn.cookielaw.org",
    "https://fonts.gstatic.com",
    "https://www.gstatic.com",
    "https://translate.googleapis.com",
    "https://www.googleadservices.com",
    "https://maps.googleapis.com",
    "https://vimeo.com",
    "https://analytics.google.com",
    "https://www.google.co.in",
    "https://www.googleoptimize.com",
    "cdn.ckeditor.com",
    "intl-tel-input.com",
    "cdn.userway.org",
    "i.vimeocdn.com",
    "img.youtube.com",
    "https://translate.google.com",
    "https://translate-pa.googleapis.com",
    "www.googletagmanager.com",
    "https://www.google-analytics.com",
    "www.google-analytics.com",
    '*.cloudfront.net',
    'connect.facebook.net',
    "https://www.googleadservices.com",
    "https://www.google.co.id",
    "https://www.google.com.pe",
    "https://www.google.co.ze",
    "https://www.google.co.za",
    "https://www.google.com.pe",
    "https://www.google.co.uk",
    'https://www.google.com.au',
    'https://www.google.ca',
    '*.google.com',
    '*.google.co.uk',
    "reddit.com",
    'https://players.brightcove.net',
    'https://googleads.g.doubleclick.net',
    "*.reddit.com",
    "*.doubleclick.net",
)

CSP_CONNECT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "onetrust.com",
    "https://geolocation.onetrust.com",
    "cdn.cookielaw.org",
    "wss://ws.hotjar.com",
    "hotjar.com",
    "hotjar.io",
    "*.hotjar.io",
    "*.hotjar.com",
    "google-analytics.com",
    "dpm.demdex.net",
    "chunderw-vpc-gll.twilio.com",
    "media.twiliocdn.com",
    "eventgw.twilio.com",
    "sdk.twilio.com",
    "twilio.com",
    "google.com",
    "www.googletagmanager.com",
    "https://www.googletagmanager.com",
    "https://www.googletagmanager.com",
    "www.googletagmanager.com",
    "maps.googleapis.com",
    "https://www.googleapis.com",
    "https://www.google.com",
    "wss://chunderw-vpc-gll.twilio.com",
    "https://translate.googleapis.com",
    "https://www.googleadservices.com",
    "https://vimeo.com",
    "https://analytics.google.com",
    "https://stats.g.doubleclick.net",
    "https://www.google-analytics.com",
    "www.google-analytics.com",
    "https://fonts.gstatic.com",
    "https://www.onelink-edge.com",
    "api.userway.org",
    "highcharts.com",
    "https://ipapi.co",
    "https://translate.google.com",
    "https://translate-pa.googleapis.com",
    "https://content.hotjar.io",
    "https://static.hotjar.com",
    "https://www.google.co.in",
    "*.ckeditor.com",
    "*.analytics.google.com",
    "*.onetrust.com",
    "*.google-analytics.com",
    '*.cloudfront.net',
    '*.userway.org',
    '*.pfizerclinicaltrials.com',
    "https://publickeyservice.keys.adm-services.goog",
    '*.google.com',
    '*.google.co.uk',
    "https://www.google.co.id",
    "https://www.google.com.pe",
    "https://www.google.co.ze",
    "https://www.google.co.za",
    "https://www.google.com.pe",
    "https://www.google.co.uk",
    'https://www.google.com.au',
    'https://www.google.ca',
    'https://www.redditstatic.com',
    '*.reddit.com',
    '*.taboola.com',
    'https://players.brightcove.net',
    "*.doubleclick.net",
)

