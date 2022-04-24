from django.urls import reverse

from myproject.common.template import active_link, pagination_url, re_active_link

EXAMPLE_HTTPS_URL = "https://example.com"
EXAMPLE_HTTP_URL = "http://example.com"
TESTSERVER_URL = "http://testserver"


class TestActiveLink:
    episodes_url = "episodes:index"

    def test_active_link_no_match(self, rf):
        url = reverse("account_login")
        req = rf.get(url)
        route = active_link({"request": req}, self.episodes_url)
        assert route.url == reverse(self.episodes_url)
        assert not route.match
        assert not route.exact

    def test_active_link_exact_match(self, rf):
        url = reverse(self.episodes_url)
        req = rf.get(url)
        route = active_link({"request": req}, self.episodes_url)
        assert route.url == reverse(self.episodes_url)
        assert route.match
        assert route.exact


class TestReActiveLink:
    about_url = "about:terms"

    def test_re_active_link_no_match(self, rf):
        url = reverse("account_login")
        req = rf.get(url)
        route = re_active_link({"request": req}, self.about_url, "/about/*")
        assert route.url == reverse(self.about_url)
        assert not route.match
        assert not route.exact

    def test_active_link_non_exact_match(self, rf):
        req = rf.get(reverse(self.about_url))
        route = re_active_link({"request": req}, self.about_url, "/about/*")
        assert route.url == reverse(self.about_url)
        assert route.match
        assert not route.exact


class TestPaginationUrl:
    def test_append_page_number_to_querystring(self, rf):

        req = rf.get("/search/", {"q": "test"})
        url = pagination_url({"request": req}, 5)
        assert url.startswith("/search/?")
        assert "q=test" in url
        assert "page=5" in url
