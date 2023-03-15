import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("incognito")
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(
    executable_path='C:\Apps\chromedriver_111\chromedriver.exe', options=option)

lista = ["https://forms.gle/LQSNw6rxJYHsx3KF6",
         "https://forms.gle/3Q3ardwA4mDbQYkX8",
         "https://forms.gle/PkRirk9Z8o82ZG9A9",
         "https://forms.gle/PQkArpqEbd8G8ne39",
         "https://forms.gle/gwcxeHPLPGtgzPFh7",
         "https://forms.gle/jwR5X3C2jcwukQDE7",
         "https://forms.gle/tHowTBK916pUvkw79",
         "https://forms.gle/7hSWLaD7UezSwg8H7",
         "https://forms.gle/2RXXq6x9pqcwv3Ea9",
         "https://forms.gle/nKHwjQe7NwsXMW6YA",
         "https://forms.gle/4Zjwaji7hN8guaRZA",
         "https://forms.gle/VkkjRuFSadPiJ64SA",
         "https://forms.gle/B2chnPVA4iwU3Vtz9",
         "https://forms.gle/stSu89KNZWJdxowS8",
         "https://forms.gle/WvC4Xt9wpKWbkMTc6",
         "https://forms.gle/dpi57agYvzYpqqaBA",
         "https://forms.gle/unJY383wNNF6Rqta9",
         "https://forms.gle/iuX8MQfyTEre7tSx9",
         "https://forms.gle/1GCq4NaJgipv6zi17",
         "https://forms.gle/spq9HjVerSKrKpDA9",
         "https://forms.gle/k52gJ4doMgRU5AhJA",
         "https://forms.gle/hNjXkQZi22pHkD4Z9",
         "https://forms.gle/ny7wNsL4S4hg6xLT8",
         "https://forms.gle/Ck3vaWKKMASsx7eo9",
         "https://forms.gle/7LQ4nqBrYphrBTaQ6",
         "https://forms.gle/3F2bjyub9UuoY9Jd7",
         "https://forms.gle/A6WSqnAGB5uDmNK77",
         "https://forms.gle/XyeZ8MC9VgefxZ1w8",
         "https://forms.gle/KcDzM7MdAUFmX73m7",
         "https://forms.gle/ntFXhz6Nnb9ftPRi9",
         "https://forms.gle/QPo6wxg4NDJoY1KP8",
         "https://forms.gle/b6NBukzM8YqTQsA99",
         "https://forms.gle/a6c31fERQj9Hn21e7",
         "https://forms.gle/91SJvXQCfXDQTkqq7",
         "https://forms.gle/LN3UfgHRxBSYhDu59",
         "https://forms.gle/w93bZXQsXBN3h6sj8",
         "https://forms.gle/5gUjFDNN3r1wpLzt8",
         "https://forms.gle/3gwEvMtQYhrVVZuWA",
         "https://forms.gle/LdxLjKmcmWvzsWgv8",
         "https://forms.gle/3SrS7SmG6Mfou4rHA",
         "https://forms.gle/5nXe5bRCkUV4QTAM6",
         "https://forms.gle/PAvWSgrvafeepRtUA",
         "https://forms.gle/J2WiBx8D9AtKVeGM6",
         "https://forms.gle/q4Zkmjy8GNhaw9sA9",
         "https://forms.gle/DU6iKmQvgDVkLEN17",
         "https://forms.gle/R2ifj8JdaJ4r9mYu5",
         "https://forms.gle/syTxpssDoydjGYG86",
         "https://forms.gle/a6c31fERQj9Hn21e7",
         "https://forms.gle/rzXpN56oJB11fYHU8",
         "https://forms.gle/qqZT8PA7CiMcFXRy5"]

random_link = random.choice(lista)

driver.get(random_link)

time.sleep(2)

one = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
one.click()

two = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
two.click()

three = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
three.click()

four = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
four.click()

five = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
five.click()

six = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
six.click()

seven = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
seven.click()

eight = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
eight.click()

nine = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
nine.click()

ten = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
ten.click()

time.sleep(2)

submit = driver.find_element(
    By.XPATH, '//*[@id = "mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
submit.click()

time.sleep(4)
