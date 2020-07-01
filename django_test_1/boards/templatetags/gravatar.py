import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = (
        f"https://www.gravatar.com/avatar/{hashlib.md5(email).hexdigest()}?"
        f"{urlencode({'d': default, 's': str(size)})}"
    )

    return url
