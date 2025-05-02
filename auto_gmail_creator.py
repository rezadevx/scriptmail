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
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid
import os
from fp.fp import FreeProxy

def get_working_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    print(f"[INFO] Menggunakan proxy: {proxy}")
    return proxy

def generate_random_name():
    first_names = ["John", "Alice", "Robert", "Sophia", "David", "Emma"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]
    return random.choice(first_names), random.choice(last_names)

def generate_random_username(first, last):
    return f"{first.lower()}.{last.lower()}{uuid.uuid4().hex[:6]}"

def generate_random_birthdate():
    return random.randint(1, 12), random.randint(1, 28), random.randint(1980, 2000)

def generate_random_gender():
    return random.choice(["Male", "Female"])

def create_account_with_proxy():
    chrome_options = ChromeOptions()

    # Buat direktori unik
    user_data_dir = f"/tmp/chrome_user_data_{uuid.uuid4()}"
    os.makedirs(user_data_dir, exist_ok=True)
    chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    proxy = get_working_proxy()
    chrome_options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

    first, last = generate_random_name()
    username = generate_random_username(first, last)
    month, day, year = generate_random_birthdate()
    gender = generate_random_gender()
    password = "SecurePassword123"

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first)
    driver.find_element(By.ID, "lastName").send_keys(last)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.NAME, "Passwd").send_keys(password)
    driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "birthMonth")))
    driver.find_element(By.ID, "birthMonth").send_keys(str(month))
    driver.find_element(By.ID, "birthDay").send_keys(str(day))
    driver.find_element(By.ID, "birthYear").send_keys(str(year))

    driver.find_element(By.XPATH, f"//div[@aria-label='{gender}']").click()
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    print(f"\n[AKUN BERHASIL DIBUAT]")
    print(f"Gmail: {username}@gmail.com")
    print(f"Password: {password}")

    driver.quit()

create_account_with_proxy()
