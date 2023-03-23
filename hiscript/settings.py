"""
Django settings for hiscript project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import dj_database_url
from pathlib import Path
import os
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [  'localhost', '127.0.0.1', 'https://hiscript-5faj.onrender.com', 'https://www.hiscript-5faj.onrender.com' ]
#CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS')
#ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://hiscript-5faj.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homesite.apps.HomesiteConfig',
    'storages',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #"whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hiscript.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
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

WSGI_APPLICATION = 'hiscript.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
}

'''
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL', default="sqlite:///db.sqlite3"))
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}
'''
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
''''
STATIC_URL = 'static/'
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS =[BASE_DIR / 'static']
STATICFILES_DIRS =(
   os.path.join(BASE_DIR, 'static'),
)


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


'''

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#USE_S3 = os.getenv('USE_S3') == 'TRUE'

#AWS settings
#if USE_S3:


AWS_LOCATION = 'static'
AWS_ACCESS_KEY_ID =os.getenv('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = { 'CacheControl': 'max-age=86400'}
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = 'hiscript.storage_backends.MediaStore'
STATICFILES_STORAGE = 'hiscript.storage_backends.StaticStorage'
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static'),
] 
STATIC_URL='https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

AWS_DEFAULT_ACL = 'public-read'

MEDIA_URL =  'media/'
MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = '/%s/' % MEDIAFILES_LOCATION
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

'''
else:
    STATIC_URL = 'static/'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATICFILES_DIRS =[BASE_DIR / 'static']
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATICFILES_DIRS =(
        os.path.join(BASE_DIR, 'static'),
    )
'''
#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'officialhiscript@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('GMAIL_SMTP')
EMAIL_PORT = 587
#EMAIL_TIMEOUT= 120
EMAIL_USE_TLS = True

#caching settings
'''
CACHES = {'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
#CACHE_MIDDLEWARE_ALIAS = 'default'  # which cache alias to use
#CACHE_MIDDLEWARE_SECONDS = 1600   # number of seconds to cache a page for (TTL)
#CACHE_MIDDLEWARE_KEY_PREFIX = ''
'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:/Users/hp250/myhiscript/hiscript/hiscript_cache',
    }
}
#Data upload Settings
DATA_UPLOAD_MAX_MEMORY_SIZE=30021440  
DATA_UPLOAD_MAX_NUMBER_FILES= 1000
DATA_UPLOAD_MAX_NUMBER_FIELDS=10000

#HTTPS SETTINGS
#SESSION_COOKIE_SECURE= True
#CSRF_COOKIE_SECURE= True
#SECURE_SSL_REDIRECT= True

#HSTS SETTINGS
#SECURE_HSTS_SECONDS= 31536000 # 1 year
#SECURE_HSTS_PRELOAD= True
#SECURE_HSTS_INCLUDE_SUBDOMAINS= True

'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simpler': {
            'format': '{levelname}{asctime} {module} {message}',
            'style': '{',          
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './logs/hiscript.log',
            'formatter': 'simpler',
        },
    },
    'loggers': {
        'django':{
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        }
        
    },
}
'''
