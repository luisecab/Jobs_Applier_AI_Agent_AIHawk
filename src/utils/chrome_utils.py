import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Import webdriver_manager
import urllib
from src.logging import logger

def chrome_browser_options():
    logger.debug("Setting Chrome browser options")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")  # Optional, useful in some environments
    options.add_argument("window-size=1200x800")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-autofill")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-cache")
    options.add_argument("--incognito")
    options.add_argument("--allow-file-access-from-files")  # Allow access to local files
    options.add_argument("--disable-web-security")         # Disable web security
    logger.debug("Using Chrome in incognito mode")
    
    return options

def init_browser() -> webdriver.Chrome:
    try:
        options = chrome_browser_options()
        # Use webdriver_manager to handle ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        logger.debug("Chrome browser initialized successfully.")
        return driver
    except Exception as e:
        logger.error(f"Failed to initialize browser: {str(e)}")
        raise RuntimeError(f"Failed to initialize browser: {str(e)}")



def HTML_to_PDF(html_content, driver):
    """
    Convert an HTML string to a PDF and return it encoded as base64.

    :param html_content: HTML code to convert.
    :param driver: Selenium WebDriver instance.
    :return: Base64 string of the generated PDF.
    :raises ValueError: If the input HTML is empty or invalid.
    :raises RuntimeError: If a WebDriver exception occurs.
    """
    # Validate HTML content
    if not isinstance(html_content, str) or not html_content.strip():
        raise ValueError("HTML content must be a non-empty string.")

    # Encode HTML as a data URL
    encoded_html = urllib.parse.quote(html_content)
    data_url = f"data:text/html;charset=utf-8,{encoded_html}"

    try:
        driver.get(data_url)
        # Wait for the page to fully load
        time.sleep(2)  # Increase if the HTML is complex

        # Execute the CDP command to print the page to PDF
        pdf_base64 = driver.execute_cdp_cmd("Page.printToPDF", {
            "printBackground": True,          # Include background graphics
            "landscape": False,               # Portrait orientation
            "paperWidth": 8.27,               # Page width in inches (A4)
            "paperHeight": 11.69,             # Page height in inches (A4)
            "marginTop": 0.8,                 # Top margin in inches (~2 cm)
            "marginBottom": 0.8,              # Bottom margin in inches (~2 cm)
            "marginLeft": 0.5,                # Left margin in inches (~1.27 cm)
            "marginRight": 0.5,               # Right margin in inches (~1.27 cm)
            "displayHeaderFooter": False,     # Do not show headers/footers
            "preferCSSPageSize": True,        # Use CSS page size
            "generateDocumentOutline": False, # Do not generate document outline
            "generateTaggedPDF": False,       # Do not generate tagged PDF
            "transferMode": "ReturnAsBase64"  # Return PDF as base64 string
        })
        return pdf_base64['data']
    except Exception as e:
        logger.error(f"WebDriver exception occurred: {e}")
        raise RuntimeError(f"WebDriver exception occurred: {e}")
