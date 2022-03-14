import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    time.sleep(5)
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_homePageTitle(self, setup):
        time.sleep(5)
        self.logger.info("********* Test_001_Login ********* ")
        self.logger.info("********* Verifying Home Page Title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.quit()
        if act_title == "Your store. Login":
            assert True
            self.driver.quit()
            self.logger.info("********* Home Page Title test is passed  *****")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.quit()
            self.logger.error("********* Home Page Title test is failed  *****")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********* Verifying Home Page Title   *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.quit()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* Login test is passed  *****")

            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.quit()
            self.logger.error("********* Login test is failed  *******")
            assert False

