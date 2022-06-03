from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver =webdriver.Chrome()
driver.get("https://dev.partner.rejareja.app/auth/login")
driver.maximize_window()

"""Test correct login"""
def test_login():
    driver.find_element(By.ID, 'username').send_keys('254701234561')
    driver.find_element(By.XPATH,"//*[contains(@type, 'password')]").send_keys('1122')
    driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]").click()
    sleep (3)
    ele=driver.find_element(By.XPATH, "//*[contains(text(), 'Select Business')]").is_displayed()
    assert ele
"""Tests creating a suppler successfully"""
def test_create_Supplier():
    driver.find_element(By.XPATH,"//*[contains(text(), 'MarketPlace - Test ')]").click()
    driver.find_element(By.XPATH,"//*[contains(text(), 'Suppliers')]").click()
    sleep (4)
    driver.find_element(By.XPATH,"//*[contains(text(), ' + Create Supplier ')]").click()
    driver.find_element(By.XPATH,"//*[@id='mat-input-1']").send_keys("Lewis Automation Supplier")
    sleep (2)
    driver.find_element(By.XPATH,"//*[@id='mat-chip-list-input-0']").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Pwani')]").click()
    driver.find_element(By.XPATH,"//*[@id='mat-input-4']").send_keys("Lewis")
    driver.find_element(By.XPATH,"//*[@id='mat-input-5']").send_keys("Mocha")
    driver.find_element(By.XPATH,"//*[@id='mat-input-6']").send_keys("lewismocha@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='mat-input-7']").send_keys("254720204040")
    driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]").click()
    sleep (3)
    ele=driver.find_element(By.XPATH, "//*[contains(text(), 'Supplier created successfully')]").is_displayed()
    assert ele

"""Tests logout"""
def test_logout():
    driver.find_element(By.XPATH,"//*[contains(text(), 'MarketPlace Admin')]").click()
    sleep (2)
    driver.find_element(By.XPATH,"//*[contains(text(), 'Sign out')]").click()

"""Tests incorrect login"""
def test_incorrect_login():
    driver.find_element(By.ID, 'username').send_keys('254734434344')
    driver.find_element(By.XPATH,"//*[contains(@type, 'password')]").send_keys('1175')
    driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]").click()
    sleep (3)
    ele=driver.find_element(By.XPATH, "//*[contains(text(), 'Incorrect login credentials')]").is_displayed()
    assert ele
   
