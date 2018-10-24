from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import datetime

now = datetime.datetime.now()
d = []
t = []
k = 0
with open('bday.txt') as input_file:
    for i, line in enumerate(input_file):
        line = line[:-1]
        d = line.split(" ")
        print(d)
        if now.month == int(d[0]) and now.day == int(d[1]):
            with open('names.txt') as x:
                for j, l in enumerate(x):

                    if i == j:
                        l = str(l)
                        print(l)
                        t.append(l)
                        k = k + 1


for i in range(0, k):
    driver = webdriver.Chrome(r'''C:\Users\Sheel9\PycharmProjects\birthdayWisher\chromedriver''')

    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 1600)

    target = str(t[i])[:-1]
    print(target)

    string = "Happy Birthday!!"

    x_arg = '//span[contains(@title, ' + '"' + target + '"' + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    print(group_title)
    group_title.click()

    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    input_box.send_keys(string+Keys.ENTER)

    # message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    #
    # message.send_keys(string)
    #
    # sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/button')[0]
    # sendbutton.click()

    driver.close()
