from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(0.5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.get('https://twitter.com/i/directory/profiles')
        time.sleep(2)
        home = bot.find_elements_by_xpath("//li[@id='global-nav-home' and @data-global-action='home']")[0]
        home.click()
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        searchbar = bot.find_elements_by_xpath("//input[@id='search-query' and @name='q']")[0]
        searchbar.clear()
        searchbar.send_keys(hashtag)
        searchbar.send_keys(Keys.RETURN)
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                time.sleep(2)
                try:
                    like_button = bot.find_elements_by_xpath("//div[@class='css-1dbjc4n r-xoduu5']")[4]
                    like_button.click()
                    time.sleep(5)
                except Exception as ex:
                    print(ex)
                    time.sleep(25)

tb = TwitterBot('emailofyouraccount', 'passwordofyouraccount')
tb.login()
tb.like_tweet("hashtagyoudlike")

# a little comment here so that there is a little change in the code boi