from django.shortcuts import render, redirect
from django.http import HttpResponse

import uuid
from shortenerApp.models import (
    UrlModel,
)


# View created for Landing Page
def LandingPageView(request):
    return render(request, "landing_page.html")


# View created to Short URL
def ShortUrlView(request):
    if request.method == 'POST':
        url = request.POST["url"]
        url_uid = str(uuid.uuid4())[:5]
        shorted_url = UrlModel(url=url, url_uid=url_uid)
        shorted_url.save()
        return HttpResponse(url_uid)


# View created for URL Validation
def UrlValidationView(request, url_id):
    url_details = UrlModel.objects.get(url_uid=url_id)
    return redirect(url_details.url)
