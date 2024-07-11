#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:42:51 2024

@author: dangkhoa
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 1. Khai bao bien browser
service = Service(executable_path="chromedriver-mac-arm64/chromedriver")
browser  = webdriver.Chrome(service = service)

cookies = [{'domain': '.facebook.com',
  'expiry': 1720001011,
  'httpOnly': False,
  'name': 'locale',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': 'vi_VN'},
 {'domain': '.facebook.com',
  'httpOnly': True,
  'name': 'checkpoint',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '%7B%22u%22%3A100082643709920%2C%22t%22%3A1719396207%2C%22step%22%3A0%2C%22n%22%3A%22knrra9LCNws%3D%22%2C%22inst%22%3A462976913133762%2C%22f%22%3A465803052217681%2C%22st%22%3A%22c%22%2C%22aid%22%3Anull%2C%22ca%22%3Anull%2C%22la%22%3A%22%22%2C%22ta%22%3A%221719396210.ch.s%3Apw.tDBFAiEA0kiqFksIS0RJxY4YTJ8Vl8jVx3Wq1g1GPzNw3dmzBoMCIAMS0MgHpsVBUz94-ra2cKkHtGgnEinSXmDvCK2uGrRf%22%2C%22tfvaid%22%3Anull%2C%22tfvasec%22%3Anull%2C%22sat%22%3Anull%2C%22idg%22%3Afalse%2C%22cidue%22%3A%22%22%2C%22tfuln%22%3Anull%2C%22tfvri%22%3Anull%2C%22ct%22%3A%22AWMrAG1O2exfHu6BUQcgJgX4fI1LP5mZZW8AcOCqdEisD7Y0JTnSh7nh5qdTlxlvruGQg905bbD2GK2YmvvohOnyfxPRSTuyUm3Z2BT0AJeGXYBMNWXsieCWsP6baTFWB2EC073TVK0zevLSxiUJ5w4oW9lWk3mvifI3diueFuSwZnb-M00_mz5VusrsbRExZwrsL5bqlAv607x-wnNuVFuZNp7QuSMEdEZPsAVWr6kTDHIsB3XYlh6nj1ABW1IM9D920jVXDGyzIFMCkZqeJ2o_kbawo5BiQ-04e8KsKZ-Byo6J-oQlF3Sba2Oy-ol1pp-SiMpAjrXLDtBWNV1p3Fy9SiH-fhnqV0rTESbwOBSEWgYJIaXisAO9z8XNRnphNgHACFLxpxyOiSXtyjK2kwVUAWE%22%2C%22s%22%3A%22AWWsosZ3oAjkFFMoZb4%22%2C%22cs%22%3A%5B%5D%2C%22ssp%22%3A1%7D'},
 {'domain': '.facebook.com',
  'expiry': 1720001007,
  'httpOnly': False,
  'name': 'wd',
  'path': '/',
  'sameSite': 'Lax',
  'secure': True,
  'value': '1200x683'},
 {'domain': '.facebook.com',
  'expiry': 1753956211,
  'httpOnly': True,
  'name': 'datr',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': 'bud7ZjoyrbBxb0jb67nTHw8R'},
 {'domain': '.facebook.com',
  'expiry': 1753956206,
  'httpOnly': True,
  'name': 'sb',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': 'bud7ZmurwdV4XYo084GA4eCC'},
 {'domain': '.facebook.com',
  'expiry': 1727172206,
  'httpOnly': True,
  'name': 'fr',
  'path': '/',
  'sameSite': 'None',
  'secure': True,
  'value': '0CEsVMcfdUUvd3uEH..Bme-du..AAA.0.0.Bme-du.AWVdiolkwdU'}]

# 2. Mở thử một trang web
browser.get("https://facebook.com")
for i in cookies:
    browser.add_cookie(i)

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element(By.ID,"email")
txtUser.send_keys("dinhdangkhoa1999@gmail.com") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element(By.ID,"pass")
txtPass.send_keys("aloha5")

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)

#credentials = browser.get_credentials()
#cookies = browser.get_cookies()
# 3. Dừng chương trình 5 giây
sleep(60)
# 4. Đóng trình duyệt
browser.close()