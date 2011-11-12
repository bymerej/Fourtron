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

STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

ROOT_URLCONF = 'fourtron.urls'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g3!c&rt2f-mvtv0ab#53*5vc=nyg8d4es!9)e(vnrlqet(5*Ar'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)