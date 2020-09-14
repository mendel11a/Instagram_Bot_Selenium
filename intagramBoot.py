import os
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.header import decode_header
import webbrowser
from time import sleep
import imaplib, email
import sys # to encode with a selected encoding
import codecs

class Bot():
    
    def __init__(self):
        PATH= "C:\Program Files (x86)\chromedriver.exe"
        self.driver= webdriver.Chrome(executable_path=PATH) # start chrome       
        self.driver.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
        sleep(5) # to wait before input something

        email_input=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        email_input.send_keys("Put your eamil")

        full_name_input=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input')
        full_name_input.send_keys('Put a full name')

        username_input=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input')
        username_input.send_keys("Put a username")

        password_input=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input')
        password_input.send_keys("Put a password")
        sleep(2)

        submit_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
        submit_btn.click()
        sleep(5)

        # add birthday
        self.year_random=str(random.randint(1,99))
        year_choose=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option['+self.year_random+']')
        year_choose.click()
        sleep(1)
        self.month_random=str(random.randint(1,11))
        month_choose=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option['+self.month_random+']')
        month_choose.click()
        sleep(1)

        self.day_random=str(random.randint(1,27))
        month_choose=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option['+self.day_random+']')
        month_choose.click()
        sleep(2)
        next_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[6]/button')
        next_btn.click()
        sleep(30)

        # gmail connection to get the code verification
        user = 'Put your eamil'
        password = 'Put the email password"'
        imap_url = 'imap.gmail.com'

        # Function to get email content part i.e its body part 
        def get_body(msg): 
            if msg.is_multipart(): 
                return get_body(msg.get_payload(0)) 
            else: 
                return msg.get_payload(None, True) 
        
        # Function to search for a key value pair  
        def search(key, value, con):  
            result, data = con.search(None, key, '"{}"'.format(value)) 
            return data 
        
        # Function to get the list of emails under this label 
        def get_emails(result_bytes): 
            msgs = [] # all the email data are pushed inside an array 
            for num in result_bytes[0].split(): 
                typ, data = con.fetch(num, '(RFC822)') 
                msgs.append(data) 
        
            return msgs 
        
        # this is done to make SSL connnection with GMAIL 
        con = imaplib.IMAP4_SSL(imap_url)  
        
        # logging the user in 
        con.login(user,password)  
        
        # calling function to check for email under this label 
        con.select('INBOX')

        # fetching emails from this user "tu**h*****1@gmail.com" 
        msgs = get_emails(search('FROM', 'no-reply@mail.instagram.com', con))
        instagram_confirmation=str(msgs[msgs.__len__()-1][0]).split('nSubject: ')[1].split(' ')[0] # the number confirmation
        
        confirmation_input=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input')
        confirmation_input.send_keys(instagram_confirmation)
        sleep(2)

        ok_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]/button')
        ok_btn.click()
        sleep(5)

        turnon_btn=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        turnon_btn.click()
        sleep(7)

        # Search after a user you want to follow
        search_user=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
        search_user.click()
        input_user=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        input_user.send_keys('Put the user you want to follow to')
        sleep(2)
        choose_user=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div')
        choose_user.click()
        sleep(10)
        follow_user=self.driver.find_element_by_xpath("//*[text()='Follow']")
        follow_user.click()

        os.system("pause") # not to close the program after input

    
    
def main():
    my_bot=Bot()

if __name__== '__main__':
    main()
