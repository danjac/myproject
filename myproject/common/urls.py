from django.urls import path

from myproject.common import views

rlpatterns = [
    path("accept-cookies/", views.accept_cookies, name="accept_cookies"),
    path("health-check/", views.health_check, name="health_check"),
    path("robots.txt", views.robots, name="robots"),
    path("favicon.ico", views.favicon, name="favicon"),
    path(".well-known/security.txt", views.security, name="security"),
]
