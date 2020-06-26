from Page.search import Search_text

class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def search_text(self):
        return Search_text(self.driver)