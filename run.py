from selenium import webdriver
import  time
from test_data import test_data
from python_class import lesson_07


driver=webdriver.Chrome()
driver.implicitly_wait(10)
#获取测试数据
url=test_data.url["url"]
user=test_data.login_page.get("username")
passwd=test_data.login_page.get("passwd")
s_key=test_data.s_key["key"]

print(url,user,passwd,s_key)

#打开页面
lesson_07.open_page(driver,url=url)

#登录
lesson_07.login_page(driver,username=user,passwd=passwd)

#执行用例
result=lesson_07.search_key(driver=driver,s_key=s_key)
if s_key in result:
    print("测试用例通过")
else:
    print("测试用例不通过")