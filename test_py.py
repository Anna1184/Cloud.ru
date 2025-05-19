from playwright.sync_api import sync_playwright


def test_page_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example" in page.title()
        page.locator("a:has-text('More information')").click()
        page.wait_for_url("https://www.iana.org/help/example-domains")
