import base64
from django import template
import os
from django.conf import settings
register = template.Library()

@register.filter
def file_to_base64(file_path):
    try:
        # If file_path is not absolute, make it absolute
        if not os.path.isabs(file_path):
            file_path = os.path.join(settings.MEDIA_ROOT, file_path)

        with open(file_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_image
    except FileNotFoundError:
        return ''