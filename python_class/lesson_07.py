
import time
#打开网站
def open_page( driver ,url):
    driver.get(url)
    driver.maximize_window()
#登录
def login_page(driver ,username,passwd):
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(passwd)
    driver.find_element_by_id("btnSubmit").click()

def search_key(driver,s_key):

    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    data_tab_id = driver.find_element_by_xpath("//a[@title='零售出库']").get_attribute("data-tab-id") + "-frame"
    print("data_tab_id:{}".format(data_tab_id))

    frame_id = driver.find_element_by_xpath("//iframe[@id='{}']".format(data_tab_id))
    print(frame_id)
    driver.switch_to.frame(frame_id)
    driver.find_element_by_id("searchNumber").send_keys(s_key)

    driver.find_element_by_xpath("//span[@class='l-btn-left']//span[text()='查询']").click()
    time.sleep(5)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    driver.quit()

    return num






