import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""
Desired Capabilities:
"""
desired_cap={
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "uiautomator2",
  "appium:app": "/Users/venkateshr/Desktop/App/Android/BH4_Release_09092022.apk",
  "appPackage": "com.dmdbrands.balancehealth",
  "appActivity": "com.dmdbrands.balancehealth.MainActivity",
  "appium:noReset": "true"
}
# set driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
time.sleep(2)

# Main page
driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='LOG IN']").click()

# Login page
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").send_keys("venkateshrv307@gmail.com")
driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").send_keys("123456")
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()
time.sleep(3)

# Home page
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='HISTORY']").click()
time.sleep(1)

driver.find_element(AppiumBy.XPATH,"//android.view.View[@index='2']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='email-forward']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='SEND']").click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='DISMISS']").click()
driver.back()
print("Pass")