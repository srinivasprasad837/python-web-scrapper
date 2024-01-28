from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# Get the current script directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the path to your ChromeDriver executable
chrome_driver_path = os.path.join(script_directory, 'drivers', 'chromedriver.exe')

try:
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to Google
    driver.get('https://www.google.com')

    # Find the search bar element by its name attribute ('q' is the name attribute for Google's search bar)
    search_bar = driver.find_element('name', 'q')

    # Type 'cat' in the search bar
    search_bar.send_keys('cat')

    # Press Enter to perform the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for a few seconds to allow the search results to load
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
