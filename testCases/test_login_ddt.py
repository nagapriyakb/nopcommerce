import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getAppurl()
    path=".//TestData/LoginData.xlsx"
    userName = ReadConfig.getAdminemail()
    password = ReadConfig.getAdminPassword()
    logger=Loggen.loggenm()
    def test_homepageTitle(self,setup):
        self.logger.info("*****************Testcase1*****************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.logger.info("*****************Verifying page title *****************")
        act_title= self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.logger.info("*****************Testcase Passed*****************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "homepageTitle.png")
            assert False
            self.logger.error("*****************Testcase Failed*****************")
            self.driver.close()

    def test_login(self,setup):
        self.logger.info("*****************Testcase2*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************Verifying Homepage title *****************")
        hometitle=self.driver.title

        if hometitle=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****************Testcase Passed*****************")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_loginn.png")
            assert False
            self.logger.error("*****************Testcase Failed*****************")


        self.lp.clickLogout()
        self.driver.close()
