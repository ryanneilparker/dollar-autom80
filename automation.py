from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import zipfile
import os

# Define the URL to download the Chrome WebDriver
chrome_webdriver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win64/chrome-win64.zip"

# Define the local path to save the ZIP file
download_path = "webdrivers/chrome.zip"

# Define the directory to extract the WebDriver to
webdriver_dir = "webdrivers"

# Check if the Chrome WebDriver already exists in the directory
if not os.path.exists(os.path.join(webdriver_dir, "chrome-win64", "chrome.exe")):
    print("Chrome WebDriver not found. Downloading...")

    # Download the Chrome WebDriver ZIP file
    response = requests.get(chrome_webdriver_url)
    with open(download_path, 'wb') as file:
        file.write(response.content)

    print("Chrome WebDriver downloaded successfully.")

    print("Extracting Chrome WebDriver...")

    # Extract the Chrome WebDriver from the ZIP file
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(webdriver_dir)

    print("Chrome WebDriver extracted successfully.")

    # Remove the downloaded ZIP file
    os.remove(download_path)
else:
    print("Chrome WebDriver already exists. Skipping download and extraction.")

# Set the path to the Chrome WebDriver executable
chrome_driver_path = os.path.join(webdriver_dir, "chrome-win64", "chrome.exe")

print(f"Chrome WebDriver path: {chrome_driver_path}")

# Set up ChromeOptions with the executable path
chrome_options = Options()
chrome_options.binary_location = chrome_driver_path

# Initialize the Chrome WebDriver with the specified options
browser = webdriver.Chrome(options=chrome_options)

url = "https://en.wikipedia.org/wiki/Main_Page"
browser.get(url)

article_count = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
print("Article Count:", article_count.text)

browser.close()



#app.dollareighty.com/posts

