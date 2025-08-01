from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

def find_panel_main():
    potential_headers = driver.find_elements(By.CLASS_NAME, "panel-header")

    for header in potential_headers:
        try:
            potential_span = header.find_element(By.TAG_NAME, "span")

            if "for specific schemes, currencies or destinations" in potential_span.text:
                print("PANEL HEADER FOUND")
                return header.find_element(By.XPATH, "..")


        except:
            return

    print("CONTAINER NOT FOUND")
    sys.exit()

def find_all_fee_settings_row():
    return panel_main.find_elements(By.CLASS_NAME, "fee-settings-row")

def find_payment_type_selector(row):
    return row.find_element(By.CSS_SELECTOR, '[class^="select__placeholder"]')


driver = webdriver.Chrome()

driver.get(str(input("Enter url of page you need to fill out: ")))

time.sleep(4)

panel_main = find_panel_main()
fee_settings_rows = find_all_fee_settings_row()

first_payment_type_selector = find_payment_type_selector(fee_settings_rows[0])

first_payment_type_selector.click()






# # Step 1: Go to first page and scrape values
# driver.get('http://localhost:3000')
# time.sleep(2)  # wait for page to load

# # Let's say you're scraping a product title
# values = [value.get_attribute("value") for value in driver.find_elements(By.CLASS_NAME, 'input_a')]
# print(values)

# driver.execute_script("window.open('about:blank', '_blank');")
# driver.switch_to.window(driver.window_handles[-1])

# # Step 2: Go to second page and input the value
# driver.get('http://localhost:3000')
# time.sleep(2)

# # Let's say you're inputting into a search box
# input_boxes = driver.find_elements(By.CLASS_NAME, 'input_b')

# for i, element in enumerate(input_boxes):
#     element.clear()
#     element.send_keys(values[i])
#     element.send_keys(Keys.RETURN)

# # Done
# time.sleep(5)

# input("Press Enter to exit and close the browser...")

