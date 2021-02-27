"""
WSGI config for SearchPlants project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # <- 加入

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SearchPlants.settings')

# 開發用 application = get_wsgi_application()
application = Cling(get_wsgi_application())
