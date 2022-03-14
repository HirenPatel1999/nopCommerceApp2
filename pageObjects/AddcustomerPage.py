import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # ADD Customer Page
    lnkCustomer_menu_xpath = "(//p[contains(text(),'Customers')])[1]"
    lnkCustomer_menuitem_xpath = "(//p[contains(text(),'Customers')])[2]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_id = "DateOfBirth"
    txtCompanyName_id = "Company"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "(//div[@class='k-list-scroller'])[2]/ul/li[1]"
    lstitemRegistered_xpath = "(//div[@class='k-list-scroller'])[2]/ul/li[4]"
    lstitemGuests_xpath = "(//div[@class='k-list-scroller'])[2]/ul/li[3]"
    lstitemVendors_xpath = "(//div[@class='k-list-scroller'])[2]/ul/li[5]"
    drpmgrOfVendor_id = "VendorId"
    txtAdminContent_id = "AdminComment"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).send_keys(role)
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("(//div[@class='k-list-scroller'])[2]/ul/li[3]").send_keys(role)
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.list-item.click()
        self.driver.exeute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_id(self.drpmgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_id(self.txtDob_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_id(self.txtAdminContent_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()