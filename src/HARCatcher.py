from browsermobproxy import Server
from src.selenium_wrapper import SeleniumWrapper
import psutil
import time
from selenium import webdriver


class HARCatcher(SeleniumWrapper):
    def __init__(self, url, har_name, browsermob_proxy_location, selector_dictionary=None, default_timeout=None, firefox_binary=None,
                 highlight=False,
                 geckodriver="geckodriver"):

        self.selector_dictionary = selector_dictionary
        self.default_timeout = default_timeout if default_timeout is not None else 30
        self.highlight = highlight

        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == "browsermob-proxy":
                proc.kill()
        options = {'port': 8090}
        # self.server = Server(path="../tools/browsermob-proxy-2.1.4/bin/browsermob-proxy", options=dict)
        self.server = Server(path=browsermob_proxy_location, options=options)

        self.server.start()
        time.sleep(1)
        self.proxy = self.server.create_proxy()
        time.sleep(1)

        profile = webdriver.FirefoxProfile()
        selenium_proxy = self.proxy.selenium_proxy()
        profile.set_proxy(selenium_proxy)
        self.driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=firefox_binary,
                                        executable_path=geckodriver)
        self.proxy.new_har(har_name)
        self.driver.get(url)

    def get_har(self):
        return self.proxy.har

    def deinit(self):
        self.server.stop()
        try:
            self.driver.quit()
        except:
            print("The driver couldn't be properly closed because of an unknown reason.")
