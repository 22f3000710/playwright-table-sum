from playwright.sync_api import sync_playwright
import re

seeds = range(51, 61)
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for seed in seeds:
        url = f"https://tds-iitm.github.io/qa-qjs-tables/seed{seed}.html"
        page.goto(url)
        numbers = page.locator("table td").all_inner_texts()
        for num in numbers:
            match = re.match(r"^\d+$", num.strip())
            if match:
                total_sum += int(num.strip())
    browser.close()

print(f"TOTAL SUM: {total_sum}")
