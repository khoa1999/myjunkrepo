#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:33:11 2024

@author: dangkhoa
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json
import os
 
def save_cookies(driver, path):
    with open(path, 'w') as file:
        json.dump(driver.get_cookies(), file)
def load_cookies(driver, path):
    with open(path, 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
def get_custom_chrome_driver(user_data_dir):
    # Setup Chrome options
    chrome_options = Options()
    
    # Add a macOS (ARM) user-agent string
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    # Add other desired options to make the browser appear more like a normal user
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    
    # Additional settings to further disguise the browser
    chrome_prefs = {
        "profile.default_content_setting_values.notifications": 1,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    # Modify the navigator.webdriver to false
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

# Example usage
current_dir = os.getcwd()
user_data_dir = os.path.join(current_dir, "chrome_profile")
driver = get_custom_chrome_driver(user_data_dir)
driver.get("https://facebook.com")
#load_cookies(driver, "cookies.json")
#driver.get("https://facebook.com")
txtUser = driver.find_element(By.ID,"email")
txtUser.send_keys("dinhdangkhoa1999@gmail.com") # <---  Điền username thật của các bạn vào đây

txtPass = driver.find_element(By.ID,"pass")
txtPass.send_keys("aloha5")
txtPass.send_keys(Keys.ENTER)
#save_cookies(driver,"cookies.json")
sleep(60)
driver.close()
