#! python3
# command line emailer.py - email a string of text
"""
Write a program that takes an email address and string of text on the command
line and then, using Selenium, logs into your email account and sends an email
of the string to the provided address. (You might want to set up a separate email
account for this program.)

Note: Dealing with email can be complicated. Many different users have different settings and
use different types of email accounts. This solution may not work for you and you will
have to find something suitable for your specific settings. Overall, there are much better
ways to send emails that you will learn later, so don't waste too much time with this code.
You probably won't use it, so as long as you understand how selenium works consider it a success
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# User input for recipient, subject, and body of the email as well as login information
email_username = input('What is your username?\n')
email_password = input('What is your password?\n')
email_recipient = input('Who would you like to send an email to?\n')
email_subject = input('What is the subject of the email?\n')
email_body = input('What would you like to say?\n')

# Open and log into email with selenium
# Unable to log in as Google detects the selenium webdriver as 'unsafe'
browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('http://mail.google.com')
login_elem = browser.find_element('id', 'identifierId')
login_elem.send_keys(email_username)
next_elem = browser.find_element('id', 'identifierNext')
next_elem.click()
time.sleep(3)
password_elem = browser.find_element('name', 'password')
password_elem.send_keys(email_password)
pw_next_elem = browser.find_element_by_id('id', 'passwordNext')
pw_next_elem.click()
time.sleep(3)

# This section will change depending on what mail you are using.
# In Gmail, use 'c' to compose, then Tab over each element, then use Ctrl-Enter to send.
# You can select an entire webpage with browser.find_element_by_tag_name('html') and
# enter your shortcut keys here. 
html_elem = browser.find_element('tag_name', 'html')
html_elem.send_keys('c')
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_recipient)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_subject)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_body)
html_elem.send_keys(Keys.ENTER)

print('Email was sent.')