from __future__ import annotations

import dataclasses
import re

from django import template
from django.conf import settings
from django.shortcuts import resolve_url

register = template.Library()


@dataclasses.dataclass
class ActiveLink:
    url: str
    match: bool = False
    exact: bool = False


@register.simple_tag(takes_context=True)
def pagination_url(context: dict, page_number: int, param: str = "page") -> str:
    """
    Inserts the "page" query string parameter with the
    provided page number into the template, preserving the original
    request path and any other query string parameters.

    Given the above and a URL of "/search?q=test" the result would
    be something like:

    "/search?q=test&page=3"
    """
    request = context["request"]
    params = request.GET.copy()
    params[param] = page_number
    return request.path + "?" + params.urlencode()


@register.simple_tag(takes_context=True)
def active_link(context: dict, url_name: str, *args, **kwargs) -> ActiveLink:
    url = resolve_url(url_name, *args, **kwargs)

    if context["request"].path == url:
        return ActiveLink(url, match=True, exact=True)

    if context["request"].path.startswith(url):
        return ActiveLink(url, match=True)

    return ActiveLink(url)


@register.simple_tag(takes_context=True)
def re_active_link(
    context: dict, url_name: str, pattern: str, *args, **kwargs
) -> ActiveLink:
    url = resolve_url(url_name, *args, **kwargs)
    if re.match(pattern, context["request"].path):
        return ActiveLink(url, match=True)

    return ActiveLink(url)


@register.simple_tag
def get_project_metadata() -> dict:
    return settings.PROJECT_METADATA
