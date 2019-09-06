"""A minimal Django application"""

import sys

from django.conf.urls import url
from django.http import HttpResponse
from django.conf import settings
from django.core.wsgi import get_wsgi_application


# settings should be configured before creating `application`
settings.configure(
    DEBUG=True,
    # default is empty string
    SECRET_KEY='42#yrs-$=s^0tkx34!sk8w=9Qmx90393$-)sleroof@mn*#w+o',
    # location of the root urlpatterns
    ROOT_URLCONF=__name__,
    # required when DEBUG is False, restricts which hosts can access this server
    ALLOWED_HOSTS=['*']
)


def index(request):
    return HttpResponse('Hello World')


# Django looks for the variable - `urlpatterns` to gather urls
urlpatterns = (
    url(r'^$', index),
)

# Should be the last line in the file before main.
# Required only if using a WSGI server like gunicorn, mod_wsgi, uWSGI.
# Not required for Django dev server.
# `application` is the keyword that WSGI servers specifically look for.
application = get_wsgi_application()


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    # arguments passed to this script are available in sys.argv
    execute_from_command_line(sys.argv)
