from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    element = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    element.send_keys("Мой ответ")

    element = browser.find_element_by_xpath("//input[@placeholder='Enter last name']") 
    element.send_keys("Мой ответ")

    element = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    element.send_keys("Мой ответ")

    file_button = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_button.send_keys(file_path)





    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()