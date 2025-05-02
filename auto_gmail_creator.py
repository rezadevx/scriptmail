# Display the banner at the beginning
print("""
===================================================
             ██████╗  ███╗   ███╗ █████╗ ██╗     
            ██╔═══██╗ ████╗ ████║██╔══██╗██║     
            ██║   ██║ ██╔████╔██║███████║██║     
            ██║   ██║ ██║╚██╔╝██║██╔══██║██║     
            ╚██████╔╝ ██║ ╚═╝ ██║██║  ██║███████╗
             ╚═════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
                                                  
       Automated Gmail Account Creator - By SHADOWHACKER
       Website: https://www.shadowhackr.com
===================================================
""")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from fp.fp import FreeProxy
import uuid
import os

# Function to get a working proxy
def get_working_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    print(f"Using proxy: {proxy}")
    return proxy

# Function to save emails to a text file
def save_email_to_file(email, password):
    with open("emails.txt", "a") as file:
        file.write(f"Gmail: {email}, Password: {password}\n")

# Function to generate a random name (First and Last)
def generate_random_name():
    first_names = ["John", "Alice", "Robert", "Sophia", "David", "Emma"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name, last_name

# Function to generate a random username based on the name
def generate_random_username(first_name, last_name):
    random_string = str(uuid.uuid4().hex[:6])  # Short random string to avoid duplicates
    return f"{first_name.lower()}.{last_name.lower()}{random_string}"

# Function to generate random birthdate
def generate_random_birthdate():
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{month}/{day}/{year}"

# Function to generate random gender
def generate_random_gender():
    return random.choice(["male", "female"])

# Initialize the Chrome WebDriver with Proxy
def create_account_with_proxy():
    # Set up Chrome options for using proxy
    chrome_options = ChromeOptions()

    # Specify a unique user data directory for each session
    user_data_dir = "/tmp/chrome_user_data_" + str(uuid.uuid4())
    os.makedirs(user_data_dir, exist_ok=True)

    chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
    
    # Get a working proxy and set it up
    proxy = get_working_proxy()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    
    # Initialize WebDriver with the given options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the sign-up page
    driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

    # Generate random user data
    first_name, last_name = generate_random_name()
    username = generate_random_username(first_name, last_name)
    birthdate = generate_random_birthdate()
    gender = generate_random_gender()

    # Fill in the account creation form
    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "username").send_keys(username)

    # Password and Confirm Password
    password = "SecurePassword123"
    driver.find_element(By.NAME, "Passwd").send_keys(password)
    driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)

    # Click Next
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # Wait for the birthdate field to be visible and fill it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "birthdateMonth")))
    driver.find_element(By.ID, "birthdateMonth").send_keys(str(birthdate.split('/')[0]))
    driver.find_element(By.ID, "birthdateDay").send_keys(str(birthdate.split('/')[1]))
    driver.find_element(By.ID, "birthdateYear").send_keys(str(birthdate.split('/')[2]))

    # Select gender (randomly chosen between male and female)
    driver.find_element(By.XPATH, f"//div[@aria-label='{gender.capitalize()}']").click()

    # Click Next
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    # Skip phone number and recovery email (if present)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "phoneNumberId")))
        driver.find_element(By.ID, "phoneNumberId").clear()
    except:
        pass

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "recoveryEmailAddress")))
        driver.find_element(By.ID, "recoveryEmailAddress").clear()
    except:
        pass

    # Agree to the terms and conditions
    agree_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    agree_button.click()

    # Print success message and save the email and password to a file
    print(f"Your Gmail successfully created:\n{{\ngmail: {username}@gmail.com\npassword: {password}\n}}")
    save_email_to_file(f"{username}@gmail.com", password)

    # Close the browser
    driver.quit()

# Call the function to create an account
create_account_with_proxy()
