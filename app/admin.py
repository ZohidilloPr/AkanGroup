from django.contrib import admin
from .models import Contact

# Register your models here.

list_filter = ['name', 'subject', 'email']

# SENDGRID_API_KEY = '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'
admin.site.register(Contact)