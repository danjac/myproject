from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = settings.ADMIN_SITE_HEADER


urlpatterns = [
    path("", include("myproject.common.urls")),
    path("account/", include("allauth.urls")),
    path("rq/", include("django_rq.urls")),
    path(f"{settings.ADMIN_URL}/postgres-metrics/", include("postgres_metrics.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]

if "debug_toolbar" in settings.INSTALLED_APPS:

    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
