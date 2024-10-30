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
    password_field.send_keys("quadrant")  # Replace with the actual password

    # Step 7: Click on the "SIGN IN" button
    sign_in_button = driver.find_element(By.NAME, "submit_btn")
    sign_in_button.click()
    
    time.sleep(2)

    # Step 8: Assert <h3> element text equals "Dashboard"
    # dashboard_header = WebDriverWait(driver, 40).until(
    #     EC.visibility_of_element_located((By.XPATH, "//h3[@class='page-title' and contains(text()=' Dashboard')]"))
    # )
    # assert dashboard_header.text == "Dashboard"

    # Steps 9 and 10: Click on the links that meet selected criteria
    # Replace criteria with actual locators or specific text if available
    link_criteria_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Compensation & Benefits")))
    link_criteria_1.click()
    
    link_criteria_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Payroll")))
    link_criteria_2.click()

    # Step 11: Click on "Generate Semi-monthly Payroll" link
    payroll_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Generate Semi-monthly Payroll")))
    payroll_link.click()

    # Step 12: Assert <label> element text equals "Cutoff Group"
    cutoff_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Cutoff Group']"))
    )
    assert cutoff_label.text == "Cutoff Group"

    # Step 13: Click on <span> with "-- Select Cutoff Group --" and Step 14: Select "Factory Overhead"
    cutoff_group_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='-- Select Cutoff Group --']")))
    cutoff_group_span.click()
    
    factory_overhead = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Factory Overhead']")))
    factory_overhead.click()

    # Step 15: Click on <span> with "-- Select Cutoff --" and Step 16: Select "2nd Cutoff"
    cutoff_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='-- Select Cutoff --']")))
    cutoff_span.click()
    second_cutoff = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='2nd Cutoff']")))
    second_cutoff.click()

    # Step 17: Click on "Period Cut-Off" text field
    period_cutoff_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "daterange")))
    driver.execute_script("arguments[0].click();", period_cutoff_field)



    # Steps 18 & 19: Select dates "6" and "20"
    # Try to select the dates by text content (adjust the XPath based on the HTML structure if necessary)
    date_6 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//td[text()='6']"))
    )
    driver.execute_script("arguments[0].click();", date_6)

    date_20 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[text()='20']"))
    )
    driver.execute_script("arguments[0].click();", date_20)

    # Step 20: Click on the "Apply" button
    time.sleep(1)  # Let page fully load or animations finish
    apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply']")))
    driver.execute_script("arguments[0].click();", apply_button)



    # Step 21: Click on the "Generate Payroll" button
    generate_payroll_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn_generate")))
    generate_payroll_button.click()

    # Step 22: Assert "Review Payroll" link text
    review_payroll_link = WebDriverWait(WebDriverWait, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Review Payroll"))
    )
    assert review_payroll_link.get_attribute("href") == "https://bonpackhr.qalphalabs.com/payroll/review"

    # Step 23: Click on "Review Payroll" link
    review_payroll_link.click()

    # Step 24: Click on the "Search:" text field and Step 25: Enter "ala"
    search_field = WebDriverWait(driver, 10).until(By.ID, "searchField")
    search_field.click()
    search_field.send_keys("ala")

    # Step 26: Click on "View Details" link
    view_details_link = WebDriverWait(driver, 10).until(By.LINK_TEXT, "View Details")
    view_details_link.click()

    # Step 27: Assert URL path equals "/payroll/details/16787/review"
    assert WebDriverWait.current_url.endswith("/payroll/details/16787/review")

    # Step 28: Click on "Review Payroll" link again
    review_payroll_link = WebDriverWait(driver, 10).until(By.LINK_TEXT, "Review Payroll")
    review_payroll_link.click()

finally:
    # Close the browser after testing
    time.sleep(3)
    driver.quit()
