from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# Set up virtual display
display = Display(visible=0, size=(1920, 1080))
display.start()

# Install ChromeDriver
chromedriver_autoinstaller.install()

# Set up Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Initialize the RecaptchaSolver
    solver = RecaptchaSolver(driver=driver)
    # Open the webpage with reCAPTCHA
    driver.get('https://www.google.com/recaptcha/api2/demo')
    # Find the reCAPTCHA iframe
    recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    # Click the reCAPTCHA checkbox
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    # Take a screenshot after solving reCAPTCHA
    driver.save_screenshot('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")
    
finally:
    # Clean up
    driver.quit()
    display.stop()
