from django.urls import path
from shortenerApp.views import (
    LandingPageView,
    ShortUrlView,
    UrlValidationView,
)


urlpatterns = [
    path('', LandingPageView, name="landing_page"),
    path('short_url', ShortUrlView, name="short_url"),
    path("<str:url_id>", UrlValidationView, name="url_validation"),
]
