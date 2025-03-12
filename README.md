# 🚀 Selenium Browser Automation with Python

## 📄 Overview

This project automates browser actions using **Selenium** in Python. The goal is to log into a webpage by:

- Opening a login page
- Entering credentials (username and password)
- Clicking the login button
- Running the script **without showing a CMD window**

A batch file (`.bat`) is used to run the script silently, while still opening the browser.

---

## 🏃‍♀️ How to Set Up

### 1. **Install Python and Selenium**

Ensure Python and Selenium are installed:

```bash
# Install Python (if not already installed)
python --version

# Install Selenium
pip install selenium
```

### 2. **Download ChromeDriver**

Make sure **ChromeDriver** matches your Chrome version:

1. Find your Chrome version:
   - Open Chrome → **Settings** → **About Chrome**
2. Download the matching ChromeDriver: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
3. Place `chromedriver.exe` in your working directory or add it to PATH.

### 3. **Python Script**

Create a `login_automation.py` file:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

# Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-insecure-localhost')

# Hide CMD window
chrome_service = Service()
chrome_service.creationflags = CREATE_NO_WINDOW

# Initialize WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the login page
driver.get("https://hfw.vitap.ac.in:8090/httpclient.html")

try:
    username = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username.send_keys("23bce9362")
    
    password = driver.find_element(By.NAME, "password")
    password.send_keys("your_password")

    login_button = driver.find_element(By.ID, "loginbutton")
    login_button.click()

except Exception as e:
    print(f"Error: {e}")

import time
time.sleep(3)

driver.quit()
```

### 4. **Create a Batch File**

To run the script without showing CMD:

1. Open **Notepad**.
2. Add this code:

```bat
@echo off
start "" pythonw "C:\Path\To\Your\login_automation.py"
```

3. Save it as `run_script.bat`.

### 5. **Create a Desktop Shortcut**

1. \*\*Right-click \*\***`run_script.bat`** → **Create Shortcut**.
2. Move the shortcut to your desktop.
3. (Optional) Right-click the shortcut → **Properties** → **Run:** select **Minimized**.
4. **Apply** and **OK**.

Now, double-clicking the shortcut will run your script without any CMD window!

---

## ✅ **Test the Setup**

To confirm `pythonw` is available:

```powershell
where pythonw
```

You should see something like:

```plaintext
C:\Users\YourName\AppData\Local\Programs\Python\Python310\pythonw.exe
```

If not, ensure Python is installed correctly and added to PATH.

---

## happy automation !!!
