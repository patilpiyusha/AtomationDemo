from generic.base_setup import BaseSetup
from generic.excel import Excel
import pytest
from pages.login_page import LoginPage
from pages.enter_time_track_page import EnterTimeTrackPage

class TestValidLogin(BaseSetup):
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        un=Excel.get_data(self.xl_path,"TestValidLogin",2,1)
        pw=Excel.get_data(self.xl_path,"TestValidLogin",2,2)
        #1. Enter invalid UN
        login_page=LoginPage(self.driver)
        login_page.set_username(un)
        #2. Enter invalid PW
        login_page.set_password(pw)
        #3. Click on login Button
        login_page.click_login_button()
        #4. Verify that error message is displyed
        displayed=login_page.verify_err_msg_is_displayed(self.wait)
        assert displayed
        print("The End")

