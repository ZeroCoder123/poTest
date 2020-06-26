from Base.Base import Base
import Page

class Search_text(Base):
    def __init__(self,driver):
        # self.base_obj = Base(driver)
        Base.__init__(self,driver)

    def search_click(self):
        self.click_element(Page.search_button)

    def search_input(self,text):
        self.input_element(Page.edit_text,text)

    def search_return(self):
        self.click_element(Page.click_ele)