import time
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_SearchCustomerByName_005_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.regression

    def test_searchCustomerByName(self, setup):
        self.logger.info("*********** SearchCustomerByName_005 ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Successful ******")

        self.logger.info("****** Starting Search Customer By Name ******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("******** searching customer by nameID *********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("******** TC_SearchCustomerByEmail_004 Finished ********")
        self.driver.quit()



