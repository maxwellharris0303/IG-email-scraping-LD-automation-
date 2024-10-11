from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
from time import sleep
import re

import quickstart



capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    udid='emulator-5554',
    appPackage='com.instagram.android',
    appActivity='.activity.MainTabActivity',
    language='en',
    locale='US',
    noReset=True,
    newCommandTimeout=3000,
)

USERNAME = ""
PASSWORD = ""

appium_server_url = 'http://localhost:4723'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

def extract_username(url):
    # Define a regular expression pattern to match the username part of the URL
    pattern = r"instagram\.com/([A-Za-z0-9_.]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

while True:
    # try:
        quickstart.main()
        profile_links = quickstart.getProfileList()
        index = quickstart.getColumnCount()

        profile_names = []
        for profile_link in profile_links:
            profile_names.append(extract_username(profile_link))

        # profile_names = profile_names[index:]
        print(profile_names)

        if len(profile_names) == 0:
            break
        
        driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)
        driver.implicitly_wait(20)
        ####################### Login start ##############################
        # username_field = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')[0]
        # username_field.send_keys(USERNAME)
        # password_field = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')[1]
        # password_field.send_keys(PASSWORD)
        # login_button = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Log in"]')
        # login_button.click()
        ####################### Login end ##############################

        search_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search and explore')
        search_button.click()

        def save_data(data, i):
            RANGE_DATA = f'Account Data!B{i + 2}:F'
            quickstart.insert_data(RANGE_DATA, data)

        for profile_name in profile_names:
            email_address = "None"
            driver.implicitly_wait(3)
            try:
                search_input = driver.find_element(AppiumBy.ID, 'com.instagram.android:id/action_bar_search_edit_text')
                search_input.click()
            except:
                driver.press_keycode(4)
                search_input = driver.find_element(AppiumBy.ID, 'com.instagram.android:id/action_bar_search_edit_text')
                search_input.click()
            # driver.implicitly_wait(5)
            search_input = driver.find_element(AppiumBy.ID, 'com.instagram.android:id/action_bar_search_edit_text')
            search_input.clear()
            search_input.send_keys(profile_name)
            try:
                result = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.instagram.android:id/row_search_user_username"]')
                result.click()
            except:
                try:
                    result = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.instagram.android:id/row_search_user_username"]')
                    result.click()
                except:
                    pass
            sleep(2)
            bio = ""
            try:
                full_name = driver.find_element(AppiumBy.ID, "com.instagram.android:id/profile_header_full_name").text
                print(f"Full Name: {full_name}")
                follower_count = driver.find_element(AppiumBy.ID, "com.instagram.android:id/row_profile_header_textview_followers_count").text
                print(f"Follower Count: {follower_count}")
                bio_element = driver.find_element(AppiumBy.ID, "com.instagram.android:id/profile_header_bio_text")
                bio = bio_element.text
                # if "… more" in bio:
                #     bio_element.click()
                #     sleep(1)
                #     bio = driver.find_element(AppiumBy.ID, "com.instagram.android:id/profile_header_bio_text").text
                print(f"Bio: {bio}")
            except:
                pass
            try:
                try:
                    email_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Email')
                    email_button.click()
                except:
                    email_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Email')
                    email_button.click()

                sleep(3)
                try:
                    recipient = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button')[2]
                    email_address = recipient.get_attribute('text')
                except:
                    sleep(3)
                    recipient = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button')[2]
                    email_address = recipient.get_attribute('text')
                
                print(email_address)
                driver.press_keycode(4)
                driver.press_keycode(4)

                back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back')
                back_button.click()
            except:
                try:
                    try:
                        subscribe_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Subscribe')
                    except:
                        subscribe_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Subscribe')
                    arrow_button = driver.find_element(AppiumBy.ID, 'com.instagram.android:id/button_image')
                    arrow_button.click()
                    try:
                        email_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Email')
                        email_button.click()
                    except:
                        driver.press_keycode(4)
                        quickstart.main()
                        index = quickstart.getColumnCount()
                        save_data(email_address, index)
                        continue

                    sleep(3)
                    try:
                        recipient = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button')[2]
                        email_address = recipient.get_attribute('text')
                    except:
                        sleep(3)
                        recipient = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button')[2]
                        email_address = recipient.get_attribute('text')
                    
                    print(email_address)

                    driver.press_keycode(4)
                    driver.press_keycode(4)

                    back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back')
                    back_button.click()
                except:
                    try:
                        contact_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Contact')
                        contact_button.click()
                        email_button = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Email"]')
                        next_sibling = driver.find_elements(AppiumBy.XPATH, '//*[@text="Email"]/following-sibling::*')[0]
                        email_address = next_sibling.get_attribute('text')
                        print(email_address)

                        back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back')
                        back_button.click()
                        back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back')
                        back_button.click()
                    except:
                        email_address = "None"
                        print(email_address)
                        back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back')
                        back_button.click()
            data = []
            data.append(profile_name)
            data.append(email_address)
            data.append(full_name)
            data.append(follower_count)
            data.append(bio)
            quickstart.main()
            index = quickstart.getColumnCount()
            save_data(data, index)
    # except:
    #     driver.quit()