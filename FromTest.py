from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Data untuk diisi di form
data_list = [
    {"First Name": "John", "Last Name": "Smith", "Company Name": "IT Solutions", "Role in Company": "Analyst", "Address": "98 North Road", "Email": "jsmith@itsolutions.co.uk", "Phone Number": "40716543298"},
    {"First Name": "Jane", "Last Name": "Dorsey", "Company Name": "MediCare", "Role in Company": "Medical Engineer", "Address": "11 Crown Street", "Email": "jdorsey@mc.com", "Phone Number": "40791345621"},
    {"First Name": "Albert", "Last Name": "Kipling", "Company Name": "Waterfront", "Role in Company": "Accountant", "Address": "22 Guild Street", "Email": "kipling@waterfront.com", "Phone Number": "40735416854"},
    {"First Name": "Michael", "Last Name": "Robertson", "Company Name": "MediCare", "Role in Company": "IT Specialist", "Address": "17 Farburn Terrace", "Email": "mrobertson@mc.com", "Phone Number": "40733652145"},
    {"First Name": "Doug", "Last Name": "Derrick", "Company Name": "Timepath Inc.", "Role in Company": "Analyst", "Address": "99 Shire Oak Road", "Email": "dderrick@timepath.co.uk", "Phone Number": "40799885412"},
    {"First Name": "Jessie", "Last Name": "Marlowe", "Company Name": "Aperture Inc.", "Role in Company": "Scientist", "Address": "27 Cheshire Street", "Email": "jmarlowe@aperture.us", "Phone Number": "40733154268"},
    {"First Name": "Stan", "Last Name": "Hamm", "Company Name": "Sugarwell", "Role in Company": "Advisor", "Address": "10 Dam Road", "Email": "shamm@sugarwell.org", "Phone Number": "40712462257"},
    {"First Name": "Michelle", "Last Name": "Norton", "Company Name": "Aperture Inc.", "Role in Company": "Scientist", "Address": "13 White Rabbit Street", "Email": "mnorton@aperture.us", "Phone Number": "40731254562"},
    {"First Name": "Stacy", "Last Name": "Shelby", "Company Name": "TechDev", "Role in Company": "HR Manager", "Address": "19 Pineapple Boulevard", "Email": "sshelby@techdev.com", "Phone Number": "40741785214"},
    {"First Name": "Lara", "Last Name": "Palmer", "Company Name": "Timepath Inc.", "Role in Company": "Programmer", "Address": "87 Orange Street", "Email": "lpalmer@timepath.co.uk", "Phone Number": "40731653845"}
]


# Inisialisasi WebDriver
driver = webdriver.Chrome()

try:
    # Buka halaman website
    driver.get("https://rpachallenge.com/")
    
    # Start Challenge
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()

    for i, data in enumerate(data_list):
        # Mengisi form berdasarkan XPath
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys(data["First Name"])
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']").send_keys(data["Last Name"])
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']").send_keys(data["Company Name"])
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']").send_keys(data["Role in Company"])
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']").send_keys(data["Address"])
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']").send_keys(data["Email"])
        driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']").send_keys(data["Phone Number"])
        
        # Submit form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        
        # Tambahkan jeda singkat untuk memastikan form telah dikirim sebelum iterasi berikutnya
        time.sleep(1)
        
        # Screenshot hasil akhir tiap input
        screenshot_name = f"rpachallenge_result_{i+1}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")

finally:
    driver.quit()

