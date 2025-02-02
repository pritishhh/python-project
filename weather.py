import bot_action
from requests_html import HTMLSession
import speech_to_text

def weather():
    s=HTMLSession()
    query="pune"
    url=f'https://www.google.com/search?q=weather+{query}'
    r=s.get(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})
    temp=r.html.find('div.vk_bk.TylWce SGNhVe span.wob_tm',first=True).text
    unit=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
    desc=r.html.find('span#wob_dc',first=True).text
    return temp+" "+ unit+" "+ desc


#span#wob_tm

'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.google.com/search?q=weather+pune"
driver.get(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})

try:
    temp_element = driver.find_element(By.ID, "wob_tm")
    print("Temperature:", temp_element.text)
except Exception as e:
    print("Temperature not found:", e)
finally:
    driver.quit()'''


