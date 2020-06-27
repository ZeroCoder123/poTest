from Base.initDriver import InitDriver
from Page.Page import Page_Obj
import pytest
import scripts
from Base.read_data import read_data
import allure

def yaml_data():
    data_list = []
    data = read_data("search_data").get("Search_Data")
    for i in data.keys():
        data_list.append((i,data.get(i).get("test")))
    return data_list

class Test_search:
    def setup_class(self):
        self.driver = InitDriver().initDriver(scripts.appPackage,scripts.appActivity)
        self.search_obj = Page_Obj(self.driver).search_text()
        self.search_obj.search_click()

    def teardown_class(self):
        self.search_obj.search_return()
        self.driver.quit()

    # @pytest.fixture()
    # @pytest.mark.run(order=1)
    # def test_search_001(self):
    #     self.search_obj.search_click()

    #@pytest.mark.usefixtures("search_001")
    # @pytest.fixture()
    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize("search_001",indirect=True)
    @allure.issue('http://www.163.com')
    @allure.testcase('https://www.baidu.com/ll')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title='这是搜索框测试')
    @pytest.mark.parametrize("num,text",yaml_data())
    def test_search_002(self,num,text):
        # print("用例编号:"+num)
        self.search_obj.search_input(text)
        self.driver.get_screenshot_as_file("./Screen/set_%s.png" % text)
        allure.attach( '我是测试步骤001的描述～～～','描述',)
        # assert "使用二十四小时" in self.driver.page_source,'出错了'
        # print(type(self.driver.page_source))

    # @pytest.mark.usefixtures("search_002")
    # def test_search_003(self):
    #     self.search_obj.search_return()