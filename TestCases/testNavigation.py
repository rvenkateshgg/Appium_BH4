import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

"""
Desired Capabilities:
"""
desired_cap={
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "uiautomator2",
  "appium:app": "/Users/venkateshr/Desktop/App/Android/BH4_4.0.0_20220819.apk",
  "appPackage": "com.dmdbrands.balancehealth",
  "appActivity": "com.dmdbrands.balancehealth.MainActivity",
  "appium:noReset": "true"
}
# set driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='LOG IN']").click()
time.sleep(1)

driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']").send_keys("venkateshrv307@gmail.com")
driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]").send_keys("123456")
eye_icon = driver.find_element(AppiumBy.XPATH,"//android.widget.Image[@text='eye_hide']").is_enabled()
print("Eye-icon:", str(eye_icon))
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,"//android.widget.Image[@text='help']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()
time.sleep(1)

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='MONTH']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='YEAR']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='TOTAL']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='WEEK']").click()
time.sleep(1)

Menu = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']")
Menu.click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='HISTORY']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@bounds='[0,88][1080,264]']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Back-Arrow']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@bounds='[0,280][1080,459]']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Back-Arrow']").click()
time.sleep(1)

actions = TouchAction(driver)
actions.press(x=528, y=1955).move_to(x=535, y=161).release().perform()
time.sleep(1)

actions = TouchAction(driver)
actions.press(x=518, y=1840).move_to(x=515, y=969).release().perform()
time.sleep(1)

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()
time.sleep(1)

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='MANUAL ENTRY']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='MONITOR SETUP']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@bounds='[11,77][280,258]']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@bounds='[24,90][178,244]']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='ACCOUNT']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='PERMISSIONS']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='INTEGRATIONS']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='REQUEST NEW INTEGRATION']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='CANCEL']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='HELP']").click()
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='close_icon']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='ACCOUNT']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.view.View[@text='LOGOUT']").click()
time.sleep(1)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG OUT']").click()
























