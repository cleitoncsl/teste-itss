from playwright.sync_api import Playwright, sync_playwright, expect

def Navegador(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

