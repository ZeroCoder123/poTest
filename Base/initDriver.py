from appium import webdriver

class InitDriver:

    def initDriver(self,appPackage,appActivity):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['deviceName'] = 'e35dc68f'
        desired_caps['deviceName'] = '127.0.0.1:21523'
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        # desired_caps['appActivity'] = 'com.oppo.settings.SettingsActivity'
        # desired_caps['appPackage'] = 'com.oppo.camera'
        # desired_caps['appActivity'] = '.Camera'
        desired_caps['unicaodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        return driver