# # open google.com
# # search campusx
# # learnwith.campusx.in
# # dsmp course page
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://google.com")
# # Wait for up to 10 seconds for the element to be located
# wait = WebDriverWait(driver, 5)
# input_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "realbox-icon-button")))

# input_element = driver.find_element(By.CLASS_NAME, "realbox-icon-button" )
# input_element.clear()
# input_element.send_keys("tech with tim" + Keys.ENTER)
# link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Tech With Tim')

# link.click()
# time.sleep(10)
# driver.quit()
# importing module
# connect python with webbrowser-chrome
