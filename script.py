from concurrent.futures import Executor
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pyautogui
import os

# Dictionary containing paths for each niche
niches = {
    "Baby": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Baby Niche\Baby Niche Brand Theme.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Baby Niche\70_Baby Products.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Baby Niche\Images"
    },
    "Cosmetics": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Cosmetics Niche\Cosmetics Niche Brand Theme.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Cosmetics Niche\30_CosmeticsProducts.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Cosmetics Niche\Images"
    },
    "Electronics": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Electronics Niche\Electronics Theme File.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Electronics Niche\30_Electronics_Zendrop.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Electronics Niche\Images"
    },
    "Fashion": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Fashion Niche\Fasion Niche Theme File.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Fashion Niche\30_FashionProducts.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Fashion Niche\Images"
    },
    "Fitness": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Fitness Niche\Fitness Niche Brand Theme.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Fitness Niche\30_ProductsFitness.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Fitness Niche\Images"
    },
    "Home": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Home Decor Niche\Home Decor Theme File.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Home Decor Niche\30_Home_Zendrop.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Home Decor Niche\Images"
    },
    "Jewelry": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Jewelry Niche\Jewelry Niche Brand Theme.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Jewelry Niche\30_JewelryProducts.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Jewelry Niche\Images"
    },
    "Pet": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Pet Niche\Pet Niche Theme File.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Pet Niche\30_Products_Zendrop.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Pet Niche\Images"
    },
    "Toys": {
        "theme": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Toys Niche\Toys Niche.zip",
        "products": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Toys Niche\30_Toys_Zendrop.csv",
        "images": r"C:\Users\moeal\OneDrive\Desktop\$29 Done For You Ecom Brand\Toys Niche\Images"
    }
}

# Present niche options to the user
print("Select a niche:")
for idx, niche in enumerate(niches.keys(), 1):
    print(f"{idx}. {niche}")

# Get user input for niche selection
while True:
    try:
        choice = int(input("Enter the number of your choice: "))
        if choice < 1 or choice > len(niches):
            raise ValueError
        break
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and", len(niches))

# Retrieve paths for theme file and products file based on user's choice
selected_niche = list(niches.keys())[choice - 1]
theme_file = niches[selected_niche]["theme"]
products_file = niches[selected_niche]["products"]
images_file = niches[selected_niche]["images"]


email = input("Enter the customer's email: ")
country = input("Enter the customer's country: ")
password = "Admin123@"

path_to_webdriver = r"C:\Users\moeal\OneDrive\Desktop\msedgedriver.exe"
service = Service(executable_path=path_to_webdriver)
driver = webdriver.Edge(service=service)

driver.get('https://shopify.pxf.io/DKzaGd')
driver.maximize_window()

# Click Start Free Trial
start_free_trial_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start free trial')]")))
start_free_trial_button.click()
time.sleep(10)

# Click Skip All
skip_all_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Polaris-Button--monochrome_14jw2")))
skip_all_button.click()

# Select Country
select_country = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Polaris-Select_ss8pm")))
select_country.click()

# Select Country using PyAutoGUI
pyautogui.write(country)

# Click enter using PyAutoGUY
pyautogui.press("enter")

# Wait a second
time.sleep(1)

# Click Next
next_button_menu = driver.find_elements(By.XPATH, "//button")
next_button_menu[-1].click() # Note that we find the button by index since it's information is not unique
time.sleep(3)

# Click Signup With Email
signup_with_email_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "account-picker__action-icon")))
signup_with_email_button.click()

# Input Email
email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "account_email")))
email_input.send_keys(email)

# Input Password
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "account_password")))
password_input.send_keys(password)

# Click Create Shopify Account
create_shopify_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "captcha__submit")))
create_shopify_account_button.click()

# Click Online Store
online_store_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Online Store")))
online_store_link.click()
time.sleep(10)

# Switch to iframe with the Add Theme button
frame = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frame[0])

# Click Add Theme
add_theme_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "UploadThemeModalActivator")))
add_theme_button.click()
time.sleep(3)

upload_zip_file_button = driver.find_elements(By.XPATH, "//button")
upload_zip_file_button[9].click() # Note that we find the button by index since it's information is not unique
time.sleep(3)

# Switch back to the main iframe
driver.switch_to.default_content()

# Switch to the iframe with the Upload File button
frames = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frames[1])

# Click Add File
add_file_button = driver.find_elements(By.XPATH, "//button")
add_file_button[1].click() # Note that we find the button by index since it's information is not unique
time.sleep(2)

# Use pyautogui to upload file
pyautogui.write(theme_file)
pyautogui.press("enter")

# Click Upload File
upload_file_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "Polaris-Button--variantPrimary_1stsb")))
upload_file_button.click()
time.sleep(10)

# Switch back to the main iframe
driver.switch_to.default_content()

# Switch to the iframe with the Publish button
frames = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frames[0])
time.sleep(30)

# Click Publish
publish_button = driver.find_elements(By.XPATH, "//button")
publish_button[7].click() # Note that we find the button by index since it's information is not unique
time.sleep(3)

# Switch to default iframe
driver.switch_to.default_content()

# Switch to the iframe with the Publish button (Confirmation)
frame = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frame[1])

# Click Publish (Confirmation)
publish_button_confirmation = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "Polaris-Button--variantPrimary_1stsb")))
publish_button_confirmation.click()
time.sleep(3)

# Switch to the main iframe
driver.switch_to.default_content()

# Click Products
products_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Products")))
products_link.click()
time.sleep(5)

# Click import
import_button = driver.find_elements(By.XPATH, "//button")
import_button[15].click()
time.sleep(2)

# Click Add File
add_product_file = driver.find_elements(By.XPATH, "//button")
add_product_file[18].click()
time.sleep(1)

# Use pyautogui to upload file
pyautogui.write(products_file)
pyautogui.press("enter")
time.sleep(2)

# Click upload and preview
upload_preview_button = driver.find_elements(By.XPATH, "//button")
upload_preview_button[20].click()
time.sleep(3)

# Click Import Products
import_products_button = driver.find_elements(By.XPATH, "//button")
import_products_button[-1].click()
time.sleep(3)

# Click Close
close_button = driver.find_elements(By.XPATH, "//button")
close_button[19].click()
time.sleep(3)

# Click Online Store
online_store_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Online Store")))
online_store_link.click()

# Click Pages
pages_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Pages")))
pages_link.click()
time.sleep(3)

# Switch to iframe with Add Page button
frames = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frames[0])

# Click Add Page
add_page_button = driver.find_elements(By.XPATH, "//a")
add_page_button[0].click()
time.sleep(3)

# Input Page Title
page_title_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "page-title")))
page_title_input.send_keys("FAQ")
time.sleep(1)

# Select FAQ
select_element = driver.find_element(By.CLASS_NAME, "Polaris-Select__Input_30ock")
select = Select(select_element)
select.select_by_value("faq")
time.sleep(1)

# Click Save
save_button = driver.find_elements(By.XPATH, "//button")
save_button[33].click()
time.sleep(3)

# Go back
go_back_button = driver.find_elements(By.XPATH, "//a") 
go_back_button[0].click()
time.sleep(3)

# Click Add Page
add_page_button = driver.find_elements(By.XPATH, "//a")
add_page_button[0].click()
time.sleep(3)

# Input Page Title
page_title_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "page-title")))
page_title_input.send_keys("Brand Story")
time.sleep(2)

# Select Brand Story
select_element = driver.find_element(By.CLASS_NAME, "Polaris-Select__Input_30ock")
select = Select(select_element)
select.select_by_value("about-us")
time.sleep(1)

# Click Save
save_button = driver.find_elements(By.XPATH, "//button")
save_button[33].click()
time.sleep(3)

# Go back
go_back_button = driver.find_elements(By.XPATH, "//a") 
go_back_button[0].click()
time.sleep(3)

# Add more pages if needed

# Click Pages
content_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Content")))
content_link.click()

# Click Files
files_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Files")))
files_link.click()
time.sleep(3)

# Click Upload Files
upload_files_button = driver.find_elements(By.XPATH, "//button")
upload_files_button[16].click()
time.sleep(3)

# Use PyAutoGUI to navigate to the images
pyautogui.write(images_file)

# Use PyAutoGUI to click enter
pyautogui.press("enter")

# Use PyAutoGUI to click the first image
pyautogui.click(x=400, y=400)

# Use PyAutoGUI to select all images
pyautogui.hotkey("ctrl", "a")

# Use PyAutoGUI to click Open
pyautogui.press("enter")

time.sleep(60) # Wait for the images to upload and then close the browser
