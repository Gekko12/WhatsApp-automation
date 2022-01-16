from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


chrome_path = '/snap/bin/chromium.chromedriver'
contact = "TestGroup"
text = "Hey, this message was sent using Selenium"
img_filepath = '/home/gaurav/Programs/Projects/WhatsApp_Automation/hexa.png'
pdf_filepath = '/home/gaurav/Programs/Projects/WhatsApp_Automation/basicscience.pdf'

small_delay = 3  #in-seconds, for buttons
long_delay = 6   #in-seconds, for processing time like img/doc processing while including path
qr_code_delay = 60   #in-seconds, in between time to scan the qr-code and start the automation

try:
    ser = Service(chrome_path)
    driver = webdriver.Chrome(service = ser)
    driver.maximize_window()
    driver.get("https://web.whatsapp.com")

    print('Supported web.whatsapp version:', 'Version 2.2149.4')
    print("Scanning QR code ......")
    time.sleep(qr_code_delay)
    print("Logged In")

    selected_contact = driver.find_element(By.XPATH, "//span[@title='"+contact+"']")
    selected_contact.click()
    time.sleep(small_delay)

    print('msg sending....')
    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@contenteditable="true"][@data-tab="10"]'
    input_box = driver.find_element(By.XPATH, inp_xpath)
    time.sleep(small_delay)
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(small_delay)
    print('msg sent')

    print('image sending.....')
    attach_xpath = '//div[@class="_26lC3"][@data-tab="10"][@title="Attach"]'
    attach_butt = driver.find_element(By.XPATH, attach_xpath)
    attach_butt.click()
    time.sleep(small_delay)

    image_xpath = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
    image_butt = driver.find_element(By.XPATH, image_xpath)
    image_butt.send_keys(img_filepath)
    time.sleep(long_delay)

    send_xpath = '//span[@data-testid="send"][@data-icon="send"]'
    send_butt = driver.find_element(By.XPATH, send_xpath)
    send_butt.click()
    time.sleep(small_delay)
    print('image sent')

    print('pdf sending.....')
    attach_xpath = '//div[@class="_26lC3"][@data-tab="10"][@title="Attach"]'
    attach_butt = driver.find_element(By.XPATH, attach_xpath)
    attach_butt.click()
    time.sleep(small_delay)

    pdf_xpath = '//input[@accept="*"][@type="file"]'
    pdf_butt = driver.find_element(By.XPATH, pdf_xpath)
    pdf_butt.send_keys(pdf_filepath)
    time.sleep(long_delay)

    send_xpath = '//span[@data-testid="send"][@data-icon="send"]'
    send_butt = driver.find_element(By.XPATH, send_xpath)
    send_butt.click()
    time.sleep(small_delay)
    print('pdf sent')

    driver.close()
    driver.quit()
except Exception as e:
    print('Error:', e)