import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
import string
import random
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.sanity

    def test_addCustomer(self, setup):
        self.logger.info("****** Test_003_AddCustomer ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****** Login Succesful ******")

        self.logger.info("****** Starting Add Customer Test *******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("******* Providing customer info ********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Hiren")
        self.addcust.setLastName("Patel")
        self.addcust.setGender("Male")
        self.addcust.setDob("04/23/1999")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminContent("This is for testing..........")
        self.addcust.clickOnSave()

        self.logger.info("******* Saving Customer Info ******** ")

        self.logger.info("********* Add customer validation started **********")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********* Add customer Test Passed *******")
        else:
            self.driver.save_screenshoots(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("**** Add customer Test Failed")
            assert True == False

        self.driver.quit()
        self.logger.info("**** Ending Test_003_AddCustomer Test ****")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))