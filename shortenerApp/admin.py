from django.contrib import admin

from shortenerApp.models import (
    UrlModel,
)


# Model created for Url for Admin Panel
class UrlModelAdmin(admin.ModelAdmin):
    list_display = ["url", "url_uid"]


# Register your models here.
admin.site.register(UrlModel, UrlModelAdmin)
