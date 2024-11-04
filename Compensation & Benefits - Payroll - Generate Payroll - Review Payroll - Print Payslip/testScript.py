from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Step 2: Visit URL
    app_url = "https://bonpackhr.qalphalabs.com/login"  # Replace with the actual URL
    driver.get(app_url)

    # Step 3: Click on the "Username" text field and Step 4: Enter "jsmoneda"
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "_username")))
    username_field.click()
    username_field.send_keys("jsmoneda")

    # Step 5: Click on the "Password" text field and Step 6: Enter the password
    password_field = driver.find_element(By.NAME, "_password")
    password_field.click()
    password_field.send_keys("quadrant")  # Reset the passwords first

    # Step 7: Click on the "SIGN IN" button
    sign_in_button = driver.find_element(By.NAME, "submit_btn")
    sign_in_button.click()
    
    time.sleep(2)

    # Steps 9 and 10: Click on the links that meet selected criteria
    link_criteria_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Compensation & Benefits")))
    link_criteria_1.click()
    
    link_criteria_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Payroll")))
    link_criteria_2.click()

    # Step 11: Click on "Generate Semi-monthly Payroll" link
    payroll_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Generate Semi-monthly Payroll")))
    payroll_link.click()


    # Step 12: Click on <span> with "-- Select Cutoff Group --" and Step 14: Select "Direct"
    cutoff_group_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='-- Select Cutoff Group --']")))
    cutoff_group_span.click()
    
    factory_overhead = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Direct Labor']")))
    factory_overhead.click()

    # Step 13: Click on <span> with "-- Select Cutoff --" and Step 16: Select "2nd Cutoff"
    cutoff_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='-- Select Cutoff --']")))
    cutoff_span.click()
    second_cutoff = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='2nd Cutoff']")))
    second_cutoff.click()

    # Step 14: Click on "Period Cut-Off" text field
    period_cutoff_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "date_from_date_to")))
    period_cutoff_field.send_keys("10/06/2024  -  10/20/2024" + Keys.RETURN) # Replace the date to generate a new payroll.

    # Step 15: Assert "Review Payroll" link text
    review_payroll_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Review Payroll"))
    )
    assert review_payroll_link.get_attribute("href") == "https://bonpackhr.qalphalabs.com/payroll/review"

    # Step 16: Click on "Review Payroll" link
    driver.execute_script("arguments[0].scrollIntoView(true);", review_payroll_link)
    driver.execute_script("arguments[0].click();", review_payroll_link)
    
    payroll_period_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "select2-cform-pay_period-container")))
    payroll_period_filter.click()
    
    payroll_period_filter_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='10/06/2024 - 10/20/2024 ( Direct Labor )']")))
    payroll_period_filter_result.click()
    
    payroll_filter_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn_filter")))
    payroll_filter_button.click()

    # Step 17: Click on the "Search:" text field and Step 18: Enter "altares"
    search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "list_table_length")))
    search_field.click()
    
    
    search_field_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Search: ']")))
    search_field_input.click()
    search_field_input.send_keys("altares" + Keys.RETURN) # Just replace the name if you want
 
    view_details_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "a[href='/payroll/details/16688/review']") # replace ID if necessary
    ))
    driver.execute_script("arguments[0].click();", view_details_link)
    
    payslip_print = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/payroll/details/review/16688/print']")))
    driver.execute_script("arguments[0].click();", payslip_print)


finally:
    print("Test Successful")
    time.sleep(3)
    driver.quit()
