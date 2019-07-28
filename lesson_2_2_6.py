from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")

x = int(browser.find_element_by_css_selector("[id='input_value']").text)

rez = calc(x)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(rez)

option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()

browser.execute_script("window.scrollBy(0, 200);", button)

option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()

print(rez)


button.click()
time.sleep(5)
browser.quit()
