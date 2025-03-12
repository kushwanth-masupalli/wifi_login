from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

# Chrome options to ignore SSL errors
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--allow-insecure-localhost')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')

# Set up ChromeDriver service to hide CMD window
chrome_service = Service()
chrome_service.creationflags = CREATE_NO_WINDOW

# Initialize the WebDriver with options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the login page
driver.get("https://hfw.vitap.ac.in:8090/httpclient.html")

# Wait until the username field is present (adjust timeout if needed)
try:
    username = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username.send_keys("23bce****")
    
    password = driver.find_element(By.NAME, "password")
    password.send_keys("your_password")

    login_button = driver.find_element(By.ID, "loginbutton")
    login_button.click()

except Exception as e:
    print(f"Error: {e}")

# Wait to observe the result
import time
time.sleep(3)

# Close the browser
driver.quit()
