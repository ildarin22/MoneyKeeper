"""
Django settings for moneykeeper project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', False))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MoneyKeeper',
    'rest_framework',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'moneykeeper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'moneykeeper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moneykeeper',
        'USER': os.environ.get('DATABASE_USER_NAME'),
        'HOST': os.environ.get('DATABASE_URL'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'PORT': 3306
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS = {
    'css': {
        'source_filenames': (
            'thirdparty/bootstrap/dist/css/bootstrap.css',
            'thirdparty/bootstrap/dist/css/bootstrap-theme.css',
            'thirdparty/angular-ui-grid/ui-grid.css',
            'thirdparty/ui-select/dist/select.css',
            'thirdparty/ng-notify/src/styles/ng-notify.css',
            'thirdparty/angular-loading-bar/build/loading-bar.css',
            'css/app_styles.css',
        ),
        'output_filename': 'css/project_styles.css',
        'variant': 'datauri',
    },
}
PIPELINE_JS = {
    'js': {
        'source_filenames': (
            'thirdparty/jquery/dist/jquery.js',
            'thirdparty/bootstrap/dist/js/bootstrap.js',
            'thirdparty/d3/d3.js',
            'thirdparty/moment/moment.js',
            'thirdparty/angular/angular.js',
            'thirdparty/ng-notify/src/scripts/ng-notify.js',
            'thirdparty/angular-filter/dist/angular-filter.js',
            'thirdparty/angular-resource/angular-resource.js',
            'thirdparty/ngstorage/ngStorage.js',
            'thirdparty/angular-loading-bar/build/loading-bar.js',
            'thirdparty/angular-ui-grid/ui-grid.js',
            'thirdparty/angular-bootstrap/ui-bootstrap.js',
            'thirdparty/angular-bootstrap/ui-bootstrap-tpls.js',
            'thirdparty/angular-ui-router/release/angular-ui-router.js',
            'thirdparty/angular-sanitize/angular-sanitize.js',
            'thirdparty/angular-http-auth/src/http-auth-interceptor.js',
            'thirdparty/n3-line-chart/build/line-chart.js',
            'thirdparty/api-check/dist/api-check.js',
            'thirdparty/angular-formly/dist/formly.js',
            'thirdparty/angular-formly-templates-bootstrap/dist/angular-formly-templates-bootstrap.js',
            'thirdparty/ui-select/dist/select.js',
            'thirdparty/angular-animate/angular-animate.js',
            'js/app.js',
            'js/services/auth.js',
            'js/services/dateFuncs.js',
            'js/services/dataSvc.js',
            'js/directives/select.js',
            'js/states.js',
            'js/filters.js',
            'js/grid.js',
            'js/modals/login.js',
            'js/summary/controller.js',
            'js/summary/chartController.js',
            'js/account/controller.js',
            'js/category/controller.js',
            'js/transaction/controller.js',
            'js/modals/common.js',
            'js/modals/addCategoryCtrl.js',
            'js/modals/addAccountCtrl.js',
            'js/modals/addTransactionCtrl.js',
        ),
        'output_filename': 'js/project_js.js',
    }
}
PIPELINE_ENABLED = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14)
}
