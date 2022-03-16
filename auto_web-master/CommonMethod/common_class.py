from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
等待方法
'''
class WaitMethod:
    def __init__(self,driver):
        self.driver=driver

    def ele_located(self,ele):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    def ele_clicable(self,ele):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ele))
            return True
        except:
            return False


class EleMethod:
    def __init__(self,driver):
        self.driver=driver

    def find(self,ele):
        return self.driver.find_element(*ele)

    def find_eles(self,ele,loc=False):
        if loc:
            return self.driver.find_elements(*ele)[loc]
        else:
            return self.driver.find_elements(*ele)

    def click(self,ele,loc=False):
        #loc：填数字，多元素时定位的位置（如果要定位多元素的第一个，填0或不填，都是用find_element方法）
        if loc:
            self.driver.find_elements(*ele)[loc].click()
        else:
            self.driver.find_element(*ele).click()
    def send_key(self,ele,key):
        self.driver.find_element(*ele).send_keys(key)

    def js(self,ele):
        '''滚动到元素可见'''
        js = self.find(ele)
        self.driver.execute_script('arguments[0].scrollIntoView();', js)

