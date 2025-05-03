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
from fp.fp import FreeProxy
import tempfile
import uuid
import random
import shutil
import time
import os

# Generate data acak
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

def get_working_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    print(f"[INFO] Menggunakan proxy: {proxy}")
    return proxy

# Fungsi utama
def create_account_with_proxy():
    # Buat folder profil sementara
    user_data_dir = tempfile.mkdtemp(prefix="chrome_profile_")
    
    try:
        # Setup opsi Chrome
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Tambahkan proxy
        proxy = get_working_proxy()
        chrome_options.add_argument(f'--proxy-server={proxy}')

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1024, 768)

        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Isi form
        first, last = generate_random_name()
        username = generate_random_username(first, last)
        password = "SecurePassword123"
        month, day, year = generate_random_birthdate()
        gender = generate_random_gender()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first)
        driver.find_element(By.ID, "lastName").send_keys(last)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.NAME, "Passwd").send_keys(password)
        driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

        # Tunggu halaman tanggal lahir
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "birthMonth")))

        driver.find_element(By.ID, "birthMonth").send_keys(str(month))
        driver.find_element(By.ID, "birthDay").send_keys(str(day))
        driver.find_element(By.ID, "birthYear").send_keys(str(year))
        driver.find_element(By.ID, "gender").send_keys(gender)

        driver.find_element(By.XPATH, "//span[text()='Next']").click()

        print("\n[BERHASIL] Akun Gmail berhasil dibuat:")
        print(f"Gmail: {username}@gmail.com")
        print(f"Password: {password}\n")

        time.sleep(10)  # Tunggu jika ingin melihat hasil di browser
        driver.quit()

    except Exception as e:
        print("[GAGAL]", e)
        if 'driver' in locals():
            driver.quit()
    finally:
        # Hapus folder sementara
        shutil.rmtree(user_data_dir, ignore_errors=True)

# Jalankan
create_account_with_proxy()