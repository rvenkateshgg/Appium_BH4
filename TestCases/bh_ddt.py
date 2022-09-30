import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Utilities import Xlutils
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

path = "/Users/venkateshr/Desktop/datadriven_bh_login1.xlsx"
rows = Xlutils.getRowcount(path , 'Sheet1')
print(rows)

driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='LOG IN']").click()
time.sleep(2)

for r in range(2, rows+1):
  username = Xlutils.readData(path,'Sheet1',r,1)
  password = Xlutils.readData(path,'Sheet1',r,2)

  email = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@index='0']")
  email.clear()
  email.send_keys(username)
  time.sleep(1)

  Password = driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@index='0'])[2]")
  Password.clear()
  Password .send_keys(password)

  login_btn = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").is_enabled()
  print("Enable:", str(login_btn))

  driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='LOG IN']").click()
  time.sleep(1)

  try:
    driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Menu']")
    print("Pass","\n")
    Xlutils.writeData(path,'Sheet1',r,3,"LoginPass")

  except:
    print("Fail","\n")
    Xlutils.writeData(path,'Sheet1',r,3,"LoginFail")



