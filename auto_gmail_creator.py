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
import random
import uuid
import time
import shutil

# Fungsi untuk menghasilkan nama acak
def generate_random_name():
    first = random.choice(["John", "Alice", "Robert", "Sophia", "David", "Emma"])
    last = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"])
    return first, last

# Fungsi untuk menghasilkan username acak
def generate_random_username(first, last):
    return f"{first.lower()}.{last.lower()}{uuid.uuid4().hex[:5]}"

# Fungsi untuk menghasilkan tanggal lahir acak
def generate_random_birthdate():
    return random.randint(1, 12), random.randint(1, 28), random.randint(1980, 2000)

# Fungsi untuk memilih gender secara acak
def generate_random_gender():
    return random.choice(["Male", "Female"])

# Fungsi untuk mendapatkan proxy gratis
def get_working_proxy():
    proxy = FreeProxy(rand=True, timeout=1).get()
    print(f"[INFO] Menggunakan proxy: {proxy}")
    return proxy

# Fungsi utama untuk membuat akun Gmail
def create_account_with_proxy():
    # Setup opsi Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Menggunakan mode headless (tanpa UI)
    
    # Menambahkan proxy
    proxy = get_working_proxy()
    chrome_options.add_argument(f'--proxy-server={proxy}')

    # Menjalankan ChromeDriver
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

# Jalankan fungsi untuk membuat akun dengan proxy
create_account_with_proxy()
