import pyautogui as py
import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

py.FAilSAFE = True

driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver")

#도마치캠핑장
driver.get("https://booking.ddnayo.com/booking-calendar?accommodationId=2642&groupId=")
driver.maximize_window()

#날짜선택창>시작일>종료일
xpath_date = ['//*[@id="container"]/div/div[1]/div[2]/div[2]/div[2]/form/div/div[1]','/html/body/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td[7]','/html/body/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[1]']

#로딩대기
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_date[0])))
time.sleep(0.5)

driver.find_element_by_xpath(xpath_date[0]).click()
driver.find_element_by_xpath(xpath_date[1]).click()
driver.find_element_by_xpath(xpath_date[2]).click()


book_info = ["김세진", "153허3400", "01072442567"]
