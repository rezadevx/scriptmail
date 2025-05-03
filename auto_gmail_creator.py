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
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid
import time

# Fungsi untuk membuat akun secara acak
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

# Mengunduh dan memasang chromedriver yang sesuai dengan versi Chrome
chromedriver_autoinstaller.install()

# Fungsi utama untuk membuat akun Gmail
def create_account_with_proxy():
    # Setup opsi Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Menjalankan ChromeDriver dengan pengaturan yang sudah ditentukan
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Akses halaman pendaftaran akun Gmail
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Isi form pendaftaran
        first, last = generate_random_name()
        username = generate_random_username(first, last)
        password = "SecurePassword123"
        month, day, year = generate_random_birthdate()
        gender = generate_random_gender()

        # Isi nama, username, dan password
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

        time.sleep(10)  # Tunggu beberapa detik untuk melihat hasilnya di browser
    except Exception as e:
        print("[GAGAL]", e)
    finally:
        # Menutup driver setelah selesai
        driver.quit()

# Jalankan fungsi untuk membuat akun
create_account_with_proxy()
