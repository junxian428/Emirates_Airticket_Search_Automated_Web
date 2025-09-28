import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.emirates.com/my/english/")
    page.get_by_role("button", name="Accept").click()
    page.get_by_label("Search flights").get_by_text("Arrival airport").click()
    page.get_by_role("textbox", name="Arrival airport").fill("VKO")
    page.keyboard.press("Enter")
    page.get_by_text("Moscow, RussiaVnukovo").click()
    page.get_by_role("button", name=" Next month").click()
    page.get_by_role("button", name=" Next month").click()
    page.get_by_role("button", name=" Next month").click()
    page.keyboard.press("Enter")
    page.keyboard.press("Enter")
    page.keyboard.press("Enter")
    page.keyboard.press("Enter")
    page.get_by_role("button", name="Thursday, 23 April").click()
    page.get_by_role("button", name=" Next month").click()
    page.get_by_role("button", name="Wednesday, 06 May").click()
    page.get_by_role("button", name="Search flights").click()
    time.sleep(10)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
