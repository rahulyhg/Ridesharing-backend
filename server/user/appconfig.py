from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

MB_ROOT = getattr(settings, 'MEDIA_FILE_ROOT',
                  os.path.join(settings.BASE_DIR, 'media_files'))

MB_STORAGE = FileSystemStorage(location=MB_ROOT)
#MEDIA_BROWSER_AUTH_FUNCTION = 'rest_mediabrowser.utils.default_auth'
