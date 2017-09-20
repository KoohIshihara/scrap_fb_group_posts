from selenium import webdriver
import time 

print("success import")

USER = "ADRESS TO LOGIN"
PASS = "PASSWORD TO LOGIN"
GROUP_NAME = "GROUP WHERE YOU GET POSTS"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

url_login = "https://m.facebook.com/login/?ref=dbl&fl"
browser.get(url_login)

#browser.save_screenshot("fb_login.png")


# input ipass
e = browser.find_element_by_id("m_login_email")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("m_login_password")
e.clear()
e.send_keys(PASS)


# send ipass
btn = browser.find_element_by_css_selector("#u_0_4 button")
btn.click()
time.sleep(1)
#browser.save_screenshot("fb_login2.png")


# to home
url_fb = "https://www.facebook.com/"
browser.get(url_fb)
#browser.save_screenshot("fb_login3.png")


# change tab for bookmarks
icon_talk = browser.find_element_by_css_selector("#bookmarks_jewel a")
icon_talk.click()
time.sleep(1)
#browser.save_screenshot("fb_login4.png")


# open 'more group'
list_target = ''
lists_bookmarks =  browser.find_elements_by_css_selector(".touchable")
for list in lists_bookmarks:
  text = list.text
  if text == "すべてのグループを表示":
    #list.click()
    print(list.text)
    list_target = list

list_target.click()
time.sleep(1)
#browser.save_screenshot("fb_login5.png")


# to secretgroup
lists_bookmarks =  browser.find_elements_by_css_selector("._2jcc")
for list in lists_bookmarks:
  text = list.text
  if text == GROUP_NAME:
    list_target = list

print(list_target.text)
parent = list_target.find_element_by_xpath('..')
parent.click()
time.sleep(1)
#browser.save_screenshot("fb_login6.png")


# get posts
posts = browser.find_elements_by_css_selector("#m_group_stories_container section article .story_body_container ._5rgt span")
for list in posts:
  text = list.text
  print(text)


'''
name = browser.find_element_by_css_selector("._606w span")
print(name.text)
'''
