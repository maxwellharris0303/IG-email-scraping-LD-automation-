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
    deviceName='127.0.0.1:4723',
    appPackage='com.instagram.android',
    appActivity='.activity.MainTabActivity',
    language='en',
    locale='US',
    noReset=True,
    newCommandTimeout=3000,
    # proxy={
    #     "httpProxy": "localhost:8080",
    #     "sslProxy": "localhost:8080"
    # }
)

USERNAME = "teamburner4@gmail.com"
PASSWORD = "Burner2024$"

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

quickstart.main()
profile_links = quickstart.getProfileList()
index = quickstart.getColumnCount()

profile_names = []
for profile_link in profile_links:
    profile_names.append(extract_username(profile_link))

print(profile_names)


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

cccc

def save_data(data, i):
    RANGE_DATA = f'Similar Account Profile Data!A{i + 2}:J'
    quickstart.insert_data(RANGE_DATA, data)

for profile_name in profile_names:
    try:
        driver.implicitly_wait(3)
        try:
            search_input = driver.find_element(AppiumBy.ID, 'com.instagram.android:id/action_bar_search_edit_text')
            search_input.click()
        except:
            driver.press_keycode(4)
            search_input = driver.find_element(AppiumBy.ID, 'com.instagram.android:id/action_bar_search_edit_text')
            search_input.click()
        driver.implicitly_wait(5)
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
        following_button = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="following"]')
        following_button.click()
        sleep(2)
        suggested_button = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Suggested"]')
        suggested_button.click()
        sleep(5)

        screen_size = driver.get_window_size()
        screen_height = screen_size['height']
        screen_width = screen_size['width']

        print(f"{screen_height} {screen_width}")

        # element_to_scroll_to = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("thewestwoodarchives")')

        flag = 0
        suggested_usernames = []
        while True:
            # Perform the scroll gesture using execute_script
            scroll_result = driver.execute_script("mobile: scrollGesture", {
                "left": 500,
                "top": 500,
                "width": screen_width / 2,
                "height": screen_width / 2,
                "direction": "down",
                "percent": 2.8
            })

            usernames = driver.find_elements(AppiumBy.XPATH, '//*[@resource-id="com.instagram.android:id/row_recommended_user_username"]')
            print(len(usernames))
            for username in usernames:
                print(username.text)
                if username.text not in suggested_usernames:
                    suggested_usernames.append(username.text)

                    data = []
                    data.append(f"https://www.instagram.com/{username.text}")
                    data.append("")
                    data.append("")
                    data.append("")
                    data.append("")
                    data.append("")
                    data.append("")
                    data.append("")
                    data.append("")
                    data.append(f"https://www.instagram.com/{profile_name}")
                    quickstart.main()
                    index = quickstart.getSuggestedTabColumnCount()
                    save_data(data, index)

            if scroll_result:
                flag = 0
            else:
                flag += 1
            
            if flag > 3:
                break
        print(suggested_usernames)
        print(len(suggested_usernames))
        
    

        driver.press_keycode(4)
    except:
        driver.press_keycode(4)
        driver.press_keycode(4)
        pass