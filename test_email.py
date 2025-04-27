import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "precision_farming.settings")
django.setup()

from django.core.mail import send_mail

send_mail(
    'Test from Ubuntu',
    'If you received this, it works!',
    'linusmksu30@gmail.com',
    ['linusmksu30@gmail.com'],
    fail_silently=False,
)