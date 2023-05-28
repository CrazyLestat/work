from selenium import webdriver
from selenium.webdriver.common.by import By

# Use Google Chrome webdriver with selenium
driver = webdriver.Chrome()

#URLs of pages to be tested
pages = [
    "post-insert",
    "post-insert-images",
    "post-insert/$idannuncio$/",
    "post-promote/i/",
    "feedback/post-publish-email/",
    "post-edit/"
]

try:
    # Loop over the tested pages
    for page in pages:
        url = "https://www.example.com/{}".format(page)

        # Go to page
        driver.get(url)

        # Check if alert is present and print results
        alert_present = driver.find_elements(By.CSS_SELECTOR, ".alert")
        if alert_present: 
            print("The alert is present on the {} page.".format(page))
        else:
            print("The alert is NOT present on the {} page.".format(page))
finally:
    # Close the
    driver.quit()