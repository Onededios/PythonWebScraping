from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://www.hackerrank.com/contests/dam-m3/compare/jolivera1")

# For waiting until the page loads
time.sleep(5)

# Take a screenshot and save it into a .png file
# with open("HackerRank_"+time.strftime("%Y-%m-%d.%H:%M:%S", time.localtime())+".png", 'wb') as f:
#    f.write(driver.get_full_page_screenshot_as_png())

# Print all the html on the terminal
print(driver.execute_script("return document.body.innerHTML;"))
driver.close()
