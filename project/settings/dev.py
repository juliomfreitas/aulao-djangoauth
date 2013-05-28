from .base import *



FACEBOOK_LOGIN_REDIRECT = "/"                                # (optional, defaults to "/")
FACEBOOK_APP_ID = "534045253320052"                          # required
FACEBOOK_APP_SECRET = "ba2eb76f03b61f60c54dd2148f34d846"     # required
FACEBOOK_SCOPE = "email"                                     # (optional, defaults to "email")




TWITTER_KEY = 'LSTsYXf46Yn6DtjbvWB9BQ'
TWITTER_SECRET = 'Xs90e9A0ournoVry2fbVWVzDxzzSwtDjjUrP4qszE'
LOGIN_URL='/twitter/login'
LOGOUT_URL='/twitter/logout'
LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'








DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable caching while in development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Add SQL statement logging in development
LOGGING['loggers']['django.db'] = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': False
}

# set up Django Debug Toolbar if installed
try:
    raise ImportError('nao uso no momento')
    import debug_toolbar  # noqa
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': lambda *args, **kwargs: True
    }
except ImportError:
    pass


# Set up django-extensions if installed
try:
    import django_extensions  # noqa
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass
