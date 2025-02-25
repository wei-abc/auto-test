import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_shop():

    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("测试23")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#su").click()
    time.sleep(2)
    driver.quit()
