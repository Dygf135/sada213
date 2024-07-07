import undetected_chromedriver as uc
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")

# Initialize the Undetected Chromedriver
driver = uc.Chrome(options=options)

try:
    # Initialize the RecaptchaSolver
    solver = RecaptchaSolver(driver=driver)
    
    # Open the webpage with reCAPTCHA
    driver.get('https://www.google.com/recaptcha/api2/demo')
    
    # Wait for the reCAPTCHA iframe to be present
    wait = WebDriverWait(driver, 10)
    recaptcha_iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]')))
    
    # Click the reCAPTCHA checkbox
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    
    # Wait a bit to ensure the reCAPTCHA is solved
    time.sleep(5)
    
    # Take a screenshot after solving reCAPTCHA
    driver.save_screenshot('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
    
finally:
    # Clean up
    driver.quit()
