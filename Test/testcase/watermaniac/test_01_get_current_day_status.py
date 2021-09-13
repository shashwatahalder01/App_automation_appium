from pages.watermaniac_page import WatermaniacPage
from testcase.watermaniac.base_test_watermaniac import BaseTest


class TestWatermaniac(BaseTest):

    def test_01_get_current_day_status(self):
        intro_page = WatermaniacPage(self.driver)
        intro_page.get_current_day_status()


# python3 -m unittest testcase.test_whatsapp_01_send_message
