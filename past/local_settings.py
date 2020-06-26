import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'uh^bna4r=m__e35$^e8@0**t7843d12l)aa&&b3n!2wt__ao8e'


DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
