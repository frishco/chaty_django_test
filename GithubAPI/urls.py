from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

urlpatterns = [
    # Dummy route. Can be removed.
    # url(r'^/', RedirectView.as_view(url='https://hackerrank.com', permanent=False)),
    url('', include('RestAPI.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)