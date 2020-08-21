                             # This Template Was Made By Author == Martennel

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot():
        def __init__(self, email, password):
            self.email = email
            self.password = password
            self.bot = webdriver.Firefox()

        def login(self):
            bot = self.bot
            bot.get('https://twitter.com/')
            time.sleep(3)
            email = bot.find_element_by_name('session[username_or_email]')
            password = bot.find_element_by_name('session[password]')
            email.clear()
            password.clear()
            email.send_keys(self.email)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(3)

        def liketweet(self, Twitiz):
            bot = self.bot
            bot.get('https://twitter.com/search?q='+Twitiz+'&src=typed_query')
            for i in range(1,3):
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)
                tweets = bot.find_elements_by_class_name('tweet')
                links = [elem.get_attribute('data-permalink-path')
                        for elem in tweets
                        ]
                for link in links:
                    bot.get('https://twitter.com/' + link)
                    try:
                        bot.find_element_by_class_name('HeartAnimation').click()
                        time.sleep(2)
                    except Exception as ex:
                        time.sleep(60)


me = TwitterBot('put your email','put your passwor')   #delete this message and put your email ,#delete this message and put your password
me.login()
me.liketweet('put your hashtag here')
