# Django settings for foursquare_explored project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = INSTALLED_APPS + (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'indexer',
    'paging',
    'sentry',
    'sentry.client',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'sentry.client.middleware.Sentry404CatchMiddleware',
)
