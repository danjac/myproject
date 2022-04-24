from __future__ import annotations

from typing import Callable
from urllib.parse import urlencode

from django.http import HttpRequest, HttpResponse
from django.utils.encoding import force_str
from django.utils.functional import SimpleLazyObject, cached_property


class BaseMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response


class CacheControlMiddleware(BaseMiddleware):
    def __call__(self, request: HttpRequest) -> HttpResponse:
        # workaround for https://github.com/bigskysoftware/htmx/issues/497
        # place after HtmxMiddleware
        response = self.get_response(request)
        if request.htmx:
            # don't override if cache explicitly set
            response.setdefault("Cache-Control", "no-store, max-age=0")
        return response
