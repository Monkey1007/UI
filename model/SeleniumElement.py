from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class _OperationElement(object):
    """
        浏览器操作封装类
    """

    def __init__(self, driver):
        self.driver = driver

    def F5(self):
        """浏览器刷新"""
        self.driver.refresh()

    def get(self, url: str):
        """请求url的参数"""
        self.driver.get(url)

    def drag(self, source, target):
        """
        元素拖拽

        :param source: 拖拽元素对象
        :param target: 拖拽元素位置
        """
        ActionChains(self.driver).drag_and_drop(source, target).perform()

class ElementLocation(_OperationElement):
    """
        浏览器元素定位封装类
    """

    def __init__(self, driver):
        super(ElementLocation, self).__init__(driver)

    def XPATH(self, element: str, param=""):
        """
        结合selenium，封装一个xpath文字元素定位
        Usage:
            ElementLocation(self.driver).XPATH(//*[text()='手机号/邮箱']/../div[1]/input!!click")
        """
        elements = element.split("!!")[0]
        type_event = element.split('!!')[1]
        if type_event == "click":
            self.driver.find_element(By.XPATH, '{}'.format(elements)).click()
        elif type_event == "send":
            self.driver.find_element(By.XPATH, '{}'.format(elements)).send_keys(param)
        elif type_event == "text":
            value = self.driver.find_element(By.XPATH, '{}'.format(elements)).text
            return value
        elif type_event == "display":
            value = self.driver.find_element(By.XPATH, '{}'.format(elements)).is_displayed()
            return value

    def CSS(self, element: str, param=""):
        """
        结合selenium，封装一个CSS

        :param element: "input[name='wd']", "input[name]".....
        :param param: send_keys里面的参数
        :return: 对应元素值
        """
        global dragF
        elements = element.split("!!")[0]
        type_event = element.split('!!')[1]
        if type_event == "click":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).click()
        elif type_event == "send":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).send_keys(param)
        elif type_event == "text":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).text
            return value
        elif type_event == "display":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).is_displayed()
            return value
        if type_event == "dragF":
            dragF = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements))
        if type_event == "dragS":
            dragS = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements))
            self.drag(dragF, dragS)


if __name__ == '__main__':
    text = "//*[text()='账号未注册']/..!!text"
    print(text.split("!!")[1])