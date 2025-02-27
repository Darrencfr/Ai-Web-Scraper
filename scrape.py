#bright data

import time
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service   

def scrape_website(website):
    print("Launching chrome browser...")

    chrome_driver_path = "./chromedriver.exe"
    options  = webdriver.ChromeOptions() #specify how the webdriver going to operate 
    driver = webdriver.Chrome(service = Service(chrome_driver_path),options=options) #setup actual driver (chrome)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source #get page source
        time.sleep(10)

        return html
    finally:
        driver.quit()
