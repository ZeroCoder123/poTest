from selenium.webdriver.support.wait import WebDriverWait


class Base:
    '''
    def init(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:21523'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['unicaodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    '''

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=10,poll=0.5):
        # return self.driver.find_element(by=loc,value=loc_value)
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))

    def is_display(self,loc):
        try:
            self.find_element(loc)
            return True
        except Exception as e:
            return False

    def click_element(self,loc):
        self.find_element(loc).click()

    def input_element(self,loc,text):
        ele = self.find_element(loc)
        ele.clear()
        ele.send_keys(text)