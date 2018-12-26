import warnings

from config_path.path_file import read_file
from selenium import webdriver

def browser(switch=False):
    """打开浏览器"""
    global driver
    path = read_file('package', 'ChromeDriver.exe')
    if switch:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        warnings.filterwarnings('ignore')
        driver = webdriver.Chrome(path, chrome_options=options)
        driver.set_window_size(1920, 1054)
    else:
        options = None
        driver = webdriver.Chrome(path, chrome_options=options)
    return driver

if __name__ == '__main__':
    import time

    driver = browser()
    driver.implicitly_wait(10)
    driver.get('https://www.scrm365.cn/#/account/login')
    js = 'document.getElementsByClassName("mu-text-field-input")[0].value="15928564313"'
    driver.execute_script(js)
    # driver.find_elements_by_xpath('//*[contains(@class,"mu-text-field-input")]')[0].send_keys('15928564313')
    driver.find_elements_by_xpath('//*[contains(@class,"mu-text-field-input")]')[1].send_keys('Li123456')
    driver.find_elements_by_xpath('//*[contains(@class,"enabled")]')[0].click()
    driver.find_elements_by_xpath('//*[contains(@class,"ivu-menu-item")]')[0].click()
    time.sleep(2)
    driver.execute_script('document.getElementsByClassName("iconfont-s ics-bangzhuzhongxin")')
    time.sleep(2)
    driver.quit()