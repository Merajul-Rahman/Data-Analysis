from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# Reusable function to safely wait for element
def wait_for_element_safely(driver, by, value, timeout=20):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except TimeoutException:
        print(f"Timeout waiting for element ({by}, {value}).")
        return None


# Reusable function for waiting for elements to be clickable
def wait_for_element(driver, by, value, timeout=20):
    try:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    except Exception as e:
        print(f"Error waiting for element ({by}, {value}): {e}")
        return None

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

# Step 1: Open login page
driver.get('https://vts.nexdecade.com/#/authentication/signin')

# Step 2: Wait and input username and password
username = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-signin/div/div/div/form/div[1]/input')
if username:
    username.send_keys('CONCEPT.KNITTING')

password = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-signin/div/div/div/form/div[2]/input')
if password:
    password.send_keys('CONCEPt@323')

# Step 3: Wait and click login button
btn = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-signin/div/div/div/form/div[3]/button')
if btn:
    btn.click()

# Step 4: Wait for the navbar toggle to appear and click it
navbar_toggle = wait_for_element(driver, By.XPATH, '//*[@id="sidebarnav"]')
if navbar_toggle:
    navbar_toggle.click()
    print('Navbar toggle clicked successfully')

# Step 5: Wait for the "Reports" button to appear and click it
reports_button = wait_for_element(driver, By.XPATH, '//*[@id="sidebarnav"]/li[12]/a', 5)
if reports_button:
    reports_button.click()
    print("Reports")

# Step 6: Wait for and click "Engine Run Time" option
engine_run_time = wait_for_element(driver, By.XPATH, '//*[@id="sidebarnav"]/li[12]/ul/li[6]', 20)
if engine_run_time:
    engine_run_time.click()
    print("Engine Run Time")

# Step 7: Select the second element of the report type dropdown
rtype_dropdown = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[2]/form/div/div[2]/ng-select', 20)
if rtype_dropdown:
    rtype_dropdown.click()  # Open the dropdown
    time.sleep(2)  # Allow the dropdown options to load

    # Locate the second option inside the dropdown
    second_option = wait_for_element(driver, By.XPATH, '//ng-dropdown-panel//div[@role="option"][2]', 10)
    if second_option:
        second_option.click()  # Click the second option
        print("Second element in the dropdown selected.")
    else:
        print("Second element in the dropdown not found.")
else:
    print("Report type dropdown not found.")

# Step 8: Set from date
fdate = wait_for_element(driver, By.XPATH, '//*[@id="fromDateTime"]', 20)
if fdate:
    fdate.send_keys('11/1/2024 00:00')
    fdate.send_keys(Keys.ENTER)
    print("From Date")

# Step 9: Set to date
tdate = wait_for_element(driver, By.XPATH, '//*[@id="toDateTime"]', 20)
if tdate:
    tdate.send_keys('12/30/2024 00:00')
    tdate.send_keys(Keys.ENTER)
    print("To Date")

# Step 10: Select vehicle
vinput = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[2]/form/div/div[1]/app-vehicle-list-form/form/ng-select/div/div/div[2]/input', 20)
if vinput:
    vinput.send_keys(' CMCHA511022')
    vinput.send_keys(Keys.ENTER)
    print("Vehicle number")



# Step 11: Click search button
search = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[2]/form/div/div[5]/button', 20)
if search:
    search.click()
    print("Search")

#step 12: Click download button
excel = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[3]/div/ul[2]/li[1]/div/button',50)
if excel:
    excel.click()


# List of vehicle numbers
vehicle_numbers = [
    'DMCHA297802', 'DMCHA518396', 'DMCHA520408', 'DMCHA520411', 
    'DMCHA520791', 'DMCHA520792', 'DMCHA520793', 'DMCHA520794', 'DMCHA520825', 
    'DMCHA520826', 'DMCHA520827', 'DMCHA521036', 'DMCHA521037', 'DMCHA521038', 
    'DMCHA521228', 'DMCHA521229', 'DMCHA521238', 'DMCHA521239', 'DMCHA521250', 
    'DMCHA521491', 'DMCHA521618', 'DMCHA521619', 'DMCHA521620', 'DMCHA521664', 
    'DMCHA521712', 'DMCHA521713', 'DMCHA521714', 'DMCHA522693', 'DMCHA533117', 
    'DMCHA534438', 'DMCHA534522', 'DMCHA535590', 'DMCHA535669', 'DMCHA535994', 
    'DMCHA538526', 'DMGA213238', 'DMGA215332', 'DMGA286283', 'DMGA290069', 
    'DMGA312787', 'DMGA337380', 'DMGA366457', 'DMGA366458', 'DMGA366460', 
    'DMGA366461', 'DMGA367077', 'DMGA367078', 'DMGA368006', 'DMGA391806', 
    'DMJHA110525', 'DMJHA120041', 'DMJHA120263', 'DMKHA128071', 'DMSHA110744', 
    'DMSHA110854'
]

for vehicle in vehicle_numbers:
    time.sleep(2)
    # Step 10: Re-locate the input field for each iteration
    vinput = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[2]/form/div/div[1]/app-vehicle-list-form/form/ng-select/div/div/div[3]/input', 20)
    time.sleep(1)
    if vinput:
        vinput.clear()  # Clear the previous input
        time.sleep(1)
        vinput.click()  # Open the dropdown
        time.sleep(1)
        vinput.send_keys(vehicle)
        time.sleep(1)  # Allow time for the dropdown to filter
        vinput.send_keys(Keys.ENTER)
        time.sleep(2)
        print(f"Vehicle number {vehicle} selected.")

    # Step 11: Click search button
    search = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[2]/form/div/div[5]/button', 20)
    if search:
        search.click()
        print(f"Search button clicked for vehicle {vehicle}.")
        time.sleep(10)  # Wait for the results to load if needed

    # Step 12: Click download button
    excel = wait_for_element(driver, By.XPATH, '/html/body/app-root/app-engine-rintime-report/section/div[2]/div/div/div/div[3]/div/ul[2]/li[1]/div/button', 50)
    if excel:
        excel.click()
        print(f"Excel download clicked for vehicle {vehicle}.")
        time.sleep(2)  # Wait for the download to start if needed
