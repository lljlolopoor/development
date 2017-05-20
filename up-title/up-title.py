from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from random import choice
import smtplib
import shutil
from email.mime.text import MIMEText

print "==============   Start ==============================="
print time.strftime("%Y%m%d %H:%M:%S", time.localtime())
print "======================================================"
print "Open webpages : https://bbs.byr.cn/#!board/ParttimeJob"
browser = webdriver.Firefox() # Get local session of firefox
browser.get("https://bbs.byr.cn/#!board/ParttimeJob") # Load page
#
elem = browser.find_element_by_id("u_login_id") # Find the query box
# input byr userid
elem.send_keys("")
elem = browser.find_element_by_id("u_login_passwd") # Find the query box
# input byr pwd
elem.send_keys("")

time.sleep(3) # Let the page load, will be added to the API

elem = browser.find_element_by_id("u_login_submit") 
elem.click()

time.sleep(3) # Let the page load, will be added to the API
elem = browser.find_element_by_id("board_search").find_element_by_name("t1")
elem.send_keys("CSL")


elem = browser.find_element_by_id("board_search").find_element_by_class_name("button")
elem.click()
time.sleep(3) # Let the page load, will be added to the API
elem = browser.find_element_by_partial_link_text("CSL")
elem.click()

time.sleep(5) # Let the page load, will be added to the API
submit_content = choice(["ddddd", "up~up~", "bd", "ddddddddddd", "upupup"])
print "Submit content :" + submit_content + " to title..... "
elem = browser.find_element_by_name("content")
elem.send_keys(submit_content)

elem = browser.find_element_by_id("quick_post").find_element_by_class_name("button")
elem.click()

time.sleep(15) # Let the page load, will be added to the API
datetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
snapshot_name= "/home/lijuan/work/up-title/" + "snapshot" + datetime
print "Get snapshot: " + snapshot_name 
browser.get_screenshot_as_file(snapshot_name)
srcPath = snapshot_name
destPath = "/var/www/html/Top-post/" + "snapshot" + datetime
shutil.copy(srcPath,destPath)
print "Snapshot link : " + "your url" + "snapshot" + datetime
time.sleep(15) # Let the page load, will be added to the API
browser.close()
browser.quit()
print "Close webpages..."
print "==============   End   ==============================="
