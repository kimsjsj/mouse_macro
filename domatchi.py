from selenium import webdriver
import pytautogui as py
import time

py.FAilSAFE = True
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

url = 'URL을 입력하세요!'
webbrowser.get(chrome_path).open(url)

a = list(py.position())
py.click(a,interval=1)

book_info = ["김세진", "153허3400", "01072442567"]
