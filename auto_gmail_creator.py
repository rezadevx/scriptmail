# Display the banner at the beginning
print("""
===================================================
 ░▒█▀▀▄░▒█▀▀▀░▒█▀▀▀█░█▀▀▄░░░▒█▀▀▄░▒█▀▀█░▒█▀▀▀█
░▒█▄▄▀░▒█▀▀▀░░▄▄▄▀▀▒█▄▄█░░░▒█░▒█░▒█░▄▄░░▀▀▀▄▄
░▒█░▒█░▒█▄▄▄░▒█▄▄▄█▒█░▒█░░░▒█▄▄█░▒█▄▄▀░▒█▄▄▄█
                                                  
       sᴇʙᴜᴀʜ ᴛᴏᴏʟs... 
  ʏᴀ ɢᴀᴛᴀᴜ ᴛᴏᴏʟs ᴀᴘᴀᴀɴ
      ᴄᴀʀɪ ᴛᴀᴜ ᴀᴊ sᴇɴᴅɪʀɪ ᴀᴡᴋᴡᴋᴡᴋᴡᴋ
===================================================
""")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid
import time

def generate_random_name():
    first = random.choice(["John", "Alice", "Robert", "Sophia", "David", "Emma"])
    last = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"])
    return first, last

def generate_random_username(first, last):
    return f"{first.lower()}.{last.lower()}{uuid.uuid4().hex[:5]}"

def generate_random_birthdate():
    return random.randint(1, 12), random.randint(1, 28), random.randint(1980, 2000)

def generate_random_gender():
    return random.choice(["Male", "Female"])

def create_account():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))

        first, last = generate_random_name()
        username = generate_random_username(first, last)
        password = "SecurePassword123"
        month, day, year = generate_random_birthdate()
        gender = generate_random_gender()

        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(first)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(last)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@name='ConfirmPasswd']").send_keys(password)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='birthMonth']")))

        driver.find_element(By.XPATH, "//select[@id='birthMonth']").send_keys(str(month))
        driver.find_element(By.XPATH, "//input[@id='birthDay']").send_keys(str(day))
        driver.find_element(By.XPATH, "//input[@id='birthYear']").send_keys(str(year))
        driver.find_element(By.XPATH, "//select[@id='gender']").send_keys(gender)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

        print("\n[BERHASIL] Akun Gmail berhasil dibuat:")
        print(f"Gmail: {username}@gmail.com")
        print(f"Password: {password}\n")

        time.sleep(10)
    except Exception as e:
        print("[GAGAL]", e)
    finally:
        driver.quit()

create_account()

