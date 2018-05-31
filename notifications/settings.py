# -*- coding: utf-8 -*-
from django.conf import settings

CONFIG_DEFAULTS = {
    'PAGINATE_BY': 20,
    'USE_JSONFIELD': False,
    'SOFT_DELETE': False
}

def get_config():
    USER_CONFIG = getattr(settings, 'DJANGO_NOTIFICATIONS_CONFIG', {})

    CONFIG = CONFIG_DEFAULTS.copy()
    CONFIG.update(USER_CONFIG)

    return CONFIG
