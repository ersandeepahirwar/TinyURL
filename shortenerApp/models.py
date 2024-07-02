from django.db import models


# Model created for URL
class UrlModel(models.Model):
    url = models.CharField(max_length=10000)
    url_uid = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Urls"

    def __str__(self):
        return self.url
