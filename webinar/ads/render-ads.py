#!/usr/bin/env python3
"""Render ad HTML files to pixel-perfect PNGs using Playwright."""
import sys
import os
sys.path.insert(0, '/Users/rachelguglietti/Library/Python/3.9/lib/python/site-packages')
from playwright.sync_api import sync_playwright

def render_ad(html_path, output_path, width=1080, height=1080):
    """Render an HTML file to a PNG at exact pixel dimensions."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=1)
        page.goto(f'file://{os.path.abspath(html_path)}')
        page.wait_for_load_state('networkidle')
        # Wait for fonts to load
        page.wait_for_timeout(1000)
        page.screenshot(path=output_path, full_page=False, type='png')
        browser.close()
        print(f'Rendered: {output_path} ({width}x{height})')

if __name__ == '__main__':
    ads_dir = '/Users/rachelguglietti/sue-landing/webinar/ads'

    # Meta V1: 30% stat - 1:1
    render_ad(
        f'{ads_dir}/meta-v1-30pct.html',
        f'{ads_dir}/SUE_Q1-2026_WEB-EN_META-V1_1x1.png',
        1080, 1080
    )
    print('Done!')
