from generic.base_setup import BaseSetup
from generic.excel import Excel
import pytest
from pages.login_page import LoginPage
from pages.enter_time_track_page import EnterTimeTrackPage

class TestValidLogin(BaseSetup):
    @pytest.mark.run(order=3)
    def test_valid_login(self):
        un=Excel.get_data(self.xl_path,"TestValidLogin",2,1)
        pw=Excel.get_data(self.xl_path,"TestValidLogin",2,2)
        #1. Enter Valid UN
        login_page=LoginPage(self.driver)
        login_page.set_username(un)
        #2. Enter Valid PW
        login_page.set_password(pw)
        #3. Click on login Button
        login_page.click_login_button()
        #4. Verify that Home page is displayed
        ett_page=EnterTimeTrackPage(self.driver)
        displayed=ett_page.click_logout_link()
        #5. Verify login page is displayed
        displayed=login_page.verify_login_page_is_displayed(self.wait)
        assert displayed

