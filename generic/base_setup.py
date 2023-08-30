import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties


class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        print("Accessing Property file")
        pptobj = Properties()
        pptobj.load(open('config.properties'))

        self.xl_path = pptobj['XL_PATH']
        print("XL Path", self.xl_path)

        usergrid = pptobj['USERGRID'].lower()
        print("User Grid", usergrid)

        gridurl = pptobj['GRIDURL']
        print("Grid URL", gridurl)

        browser = pptobj['BROWSER'].lower()
        print("Browser", browser)
        appurl = pptobj['APPURL']
        print("App Url", appurl)
        ito = pptobj['IMPLICIT_TIME_OUT']
        print("ITO", ito)
        eto = pptobj['EXPLICIT_TIME_OUT']
        print("ETO", eto)

        if usergrid == 'yes':
            print("Executing in remote system")
            if browser == 'chrome':
                print("Open Chrome Browser")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.ChromeOptions())

            elif browser == 'firefox':
                print("Open Firefox Browser")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.FirefoxOptions())
            else:
                print("Open Edge Browser")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.EdgeOptions())
        else:
            print("Executing in local system")
            if browser == 'chrome':
                print("Open Chrome Browser")
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                print("Open Firefox Browser")
                self.driver = webdriver.Firefox()
            else:
                print("Open Edge Browser")
                self.driver = webdriver.Edge()
        print("Enter the URL", appurl)
        self.driver.get(appurl)
        print("Maximize the browser")
        self.driver.maximize_window()
        print("Set ITO", ito, 'Seconds')
        self.driver.implicitly_wait(ito)
        print("Set ETO", eto, 'Seconds')
        self.wait = WebDriverWait(self.driver, eto)

    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.close()