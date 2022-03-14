import time
import pytest
from selenium import webdriver
# import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XlUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData2.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_login_ddt(self, setup):
        self.logger.info("******** Test_002_DDT_Login  **********")
        self.logger.info("********* Verifying Login DDT Title   *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XlUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)

        lst_status = []  # Empty list variable

        for r in range(2, self.rows+1):
            self.user = XlUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setpassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.quit()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            self.driver.quit()
            assert False

        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("******** Completed TC_LoginDDT_002 ********")


