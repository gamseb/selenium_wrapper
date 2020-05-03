import unittest
from src.selenium_wrapper import SeleniumWrapper
from src.HARCatcher import HARCatcher

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)

class SeleniumWrapperTest(unittest.TestCase):
    def test_search_for_text(self):

        selenium_wrapper = SeleniumWrapper("https://selenium-python.readthedocs.io/")
        try:
            text = selenium_wrapper.find_element(("xpath", "/html/body/div[1]/div[1]/div/div/div[1]/h1")).text
            # print(text)
        finally:
            selenium_wrapper.deinit()
        self.assertEqual("Selenium with Python", text)
        # self.assertEqual("Selenium wgwagwaadwada", text)

class HARCatcherTest(unittest.TestCase):
    def test_get_har(self):
        har_catcher = HARCatcher("https://darknetdiaries.com/", "darknet diaries")

        print(har_catcher.get_har())






if __name__ == '__main__':
    unittest.main()
