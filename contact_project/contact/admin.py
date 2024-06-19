from django.contrib import admin

from contact.models import Category, ContactMessage

# Register your models here.

admin.site.register(Category)
admin.site.register(ContactMessage)