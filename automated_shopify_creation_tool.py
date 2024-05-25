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

def wait_and_click(driver, by, value, timeout=30):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

def click_button_by_index(driver, tag, index, timeout=30):
    # Wait for the page to load
    elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.TAG_NAME, tag)))
    elements[index].click()

def wait_and_send_keys(driver, by, value, keys, timeout=30):
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    element.send_keys(keys)
    return element

driver.get('https://shopify.pxf.io/DKzaGd')
driver.maximize_window()

# Click Start Free Trial
wait_and_click(driver, By.XPATH, "//button[contains(text(), 'Start free trial')]")

# Click Skip All
wait_and_click(driver, By.CLASS_NAME, "Polaris-Button--monochrome_14jw2")

# Select Country
wait_and_click(driver, By.CLASS_NAME, "Polaris-Select_ss8pm")
pyautogui.write(country)
pyautogui.press("enter")

click_button_by_index(driver, "button", -1)

# Click Signup With Email
wait_and_click(driver, By.CLASS_NAME, "account-picker__action-icon")

# Input Email
wait_and_send_keys(driver, By.ID, "account_email", email)

# Input Password
wait_and_send_keys(driver, By.ID, "account_password", password)

# Click Create Shopify Account
wait_and_click(driver, By.CLASS_NAME, "captcha__submit")

# Click Content
wait_and_click(driver, By.LINK_TEXT, "Content")

# Click Files
wait_and_click(driver, By.LINK_TEXT, "Files")
time.sleep(2)

# Click Upload Files
click_button_by_index(driver, "button", 16)
time.sleep(1)

# Use PyAutoGUI to navigate to the images
pyautogui.write(images_file)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

# Use PyAutoGUI to click the first image
pyautogui.click(x=400, y=400)
time.sleep(1)

# Use PyAutoGUI to select all images
pyautogui.hotkey("ctrl", "a")
time.sleep(1)

# Use PyAutoGUI to click Open
pyautogui.press("enter")

# Wait for images to finish uploading
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "_HeaderIcon-success_ybful_66")))

# Click Online Store
wait_and_click(driver, By.LINK_TEXT, "Online Store")
time.sleep(5)

# Switch to iframe with the Add Theme button
frame = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frame[0])
time.sleep(1)

# Scroll a bit to make the Add Theme button visible
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(1)

# Click Add Theme
wait_and_click(driver, By.ID, "UploadThemeModalActivator")
time.sleep(1)

# Click Add File
click_button_by_index(driver, "button", 10)
time.sleep(1)

# Switch back to the main iframe
driver.switch_to.default_content()

# Switch to the iframe with the Upload File button
frames = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frames[1])
time.sleep(1)

# Click Add File
click_button_by_index(driver, "button", 1)
time.sleep(1)

# Use pyautogui to upload file
pyautogui.write(theme_file)
time.sleep(1)
pyautogui.press("enter")

# Click Upload File
wait_and_click(driver, By.CLASS_NAME, "Polaris-Button--variantPrimary_1stsb")

# Switch back to the main iframe
driver.switch_to.default_content()

# Switch to the iframe with the Publish button
frames = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frames[0])

# Wait for the theme to upload and then click Publish
time.sleep(35)
click_button_by_index(driver, "button", 7)

# Switch to the default iframe
driver.switch_to.default_content()

# Switch to the iframe with the Publish button (Confirmation)
frame = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frame[1])

# Click Publish (Confirmation)
wait_and_click(driver, By.CLASS_NAME, "Polaris-Button--variantPrimary_1stsb")
time.sleep(1)

# Switch to the main iframe
driver.switch_to.default_content()

# Click Products
wait_and_click(driver, By.LINK_TEXT, "Products")
time.sleep(5)

# Click Import
click_button_by_index(driver, "button", 15)
time.sleep(1)

# Click Add File
click_button_by_index(driver, "button", 18)
time.sleep(1)

# Use pyautogui to upload file
pyautogui.write(products_file)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

# Click upload and preview
click_button_by_index(driver, "button", 20)
time.sleep(5)

# Wait for the import process and click Import Products
click_button_by_index(driver, "button", -1)
time.sleep(5)

# Click Close
click_button_by_index(driver, "button", 19)
time.sleep(1)

# Click Online Store
wait_and_click(driver, By.LINK_TEXT, "Online Store")

# Click Pages
wait_and_click(driver, By.LINK_TEXT, "Pages")
time.sleep(5)

# Switch to iframe with Add Page button
frames = driver.find_elements(By.XPATH, "//iframe")
driver.switch_to.frame(frames[0])

# Click Add Page
click_button_by_index(driver, "a", 0)

# Input Page Title
wait_and_send_keys(driver, By.ID, "page-title", "FAQ")

# Select FAQ
select_element = driver.find_element(By.CLASS_NAME, "Polaris-Select__Input_30ock")
select = Select(select_element)
select.select_by_value("faq")

# Click Save
click_button_by_index(driver, "button", 33)

# Go back
click_button_by_index(driver, "a", 0)

# Click Add Page
click_button_by_index(driver, "a", 0)

# Input Page Title
wait_and_send_keys(driver, By.ID, "page-title", "Brand Story")

# Select Brand Story
select_element = driver.find_element(By.CLASS_NAME, "Polaris-Select__Input_30ock")
select = Select(select_element)
select.select_by_value("about-us")

# Click Save
click_button_by_index(driver, "button", 33)

# Go back
click_button_by_index(driver, "a", 0)

# Add more pages if needed

# Close the browser after a delay to ensure completion
WebDriverWait(driver, 60).until_not(EC.presence_of_element_located((By.CLASS_NAME, "Polaris-Spinner")))
driver.quit()
