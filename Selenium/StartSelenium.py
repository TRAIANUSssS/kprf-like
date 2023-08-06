import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def create_driver(headless=True, folder="Cookies", dr="chromedriver.exe", port="9220"):
    s = Service(f"{os.getcwd()}/{dr}")
    # some options for deiver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

    if headless:
        chrome_options.add_argument('--headless=new')  # headless or not
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('window-size=800x600')  # resolution

    chrome_options.add_argument(f'--remote-debugging-port={port}')
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--v=99")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("prefs", prefs)

    # chrome_options.add_argument(f"--user-data-dir=C:/Users/CL/PycharmProjects/kprf-like/{folder}")
    # chrome_options.add_argument("--start-maximized")  # maximized or not

    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.set_window_size(1280, 1280)

    return driver
