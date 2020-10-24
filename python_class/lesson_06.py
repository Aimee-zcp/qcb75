"""
xpath 元素定位

在开发者工具中用crtl+回车就可以确认标歹势是否有效
1.绝对定位/相对定位
绝对路径：/html/body/div/div/div[1]/a/b  ---根节点，顺序性，继承关系---失效
绝对定位面试不问，工作也不用

相对定位： 只靠自己的特征定位   用//开头+自己关心的父类

标签名+属性=//标签名[@属性名=属性值]
eg：//input[@id='username']   ---xpath表达方式

2.层级定位：
//标签名[@属性值]//标签名[@属性名=属性值]
eg：//div[@class="login-logo"]//b

 eg：//div[text()='零售出库']/..   #通过元素找到它的爸爸

3.文本属性定位：//b[text()='柠檬ERP']

4.包含属性值：//标签名[contains(@属性名/text(),属性值)]
eg：//input[contains(@class,"username")]
eg： //div[contains(@class,"login-logo")]//b
    //b[contains(text(),"柠檬")]  ---用的比较少一些
元素定位：
 元素定位八大方法，最常用的：id，name，xpath，css，class，tag，link，partial_link

 eg: username=driver.find_element_by_id("username")

 找到元素后的操作：
 点击： click
 输入内容：send_keys
 获取文本：text
 获取属性：attribute

 但凡是切换了页面。页面没有加载完，元素不显示==最好加个等待
 三种方式：
 1.强制等待：time.sleep（）
 2.隐式等待：
    可以设置一个等待时间，在这个等待时间结束之前元素就找到了，不继续等待，继续执行下面的代码：--灵活
  注意：一个session里只执行一次，整个会话都会生效#
   driver.implicitly_wait(10) #隐式等待，默认等待10s，最多等待10s，提前出现了就不继续等了
   显示等待：expected_condition----某个元素的等待


   总结：
   八大元素定位方式
   三大等待
   四大操作

  1.识别是否又子页面的方式：页面层级路径出现了iframe：就需要去切换iframe，才可以进行元素定位
  2.怎么去切换：
   1）找到这个iframe元素，切换
#窗口切换
1.通过id直接进行切换
#driver.switch_to.frame(data_tab_id)
2.通过元素定位（xpath）来切换iframe
#frame_id=driver.find_element_by_xpath("//iframe[@id='{}']".format(data_tab_id))
#driver.switch_to.frame(frame_id)
3.通过iframe的下标，从零开始， html-页面=0 第一个宝宝为1， 第二个宝宝为2

web自动化--实现正常核心功能


注意：如果id不是固定的就需要重新定位



"""

from selenium import webdriver
import  time

driver=webdriver.Chrome()

driver.implicitly_wait(10) #隐式等待，默认等待10s，最多等待10s，提前出现了就不继续等了

driver.get("http://erp.lemfix.com/login.html")

driver.maximize_window()
page_title=driver.title
print("页面title：{}".format(page_title))

text1=driver.find_element_by_xpath("//div[contains(@class,'login-logo')]//b").text #找到这个元素的位置后获取改标签的值

if(text1=="柠檬ERP"):
    print("这个页面的标题是：{}".format(text1))
else:
    print("这个测试用例不通过")


driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()

#time.sleep(5)

user=driver.find_element_by_xpath("//div[@class='pull-left info']//p").text
if user=="测试用户":
    print("这是一个测试用户")
else:
    print("这条测试用例不通过，不是测试用户")

#点击零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()

#driver.find_element_by_id("searchNumber").send_keys("314")

#获取零售出库的data_tab_id
data_tab_id=driver.find_element_by_xpath("//a[@title='零售出库']").get_attribute("data-tab-id")+"-frame"
print("data_tab_id:{}".format(data_tab_id))
#窗口切换
#1.通过id直接进行切换
#driver.switch_to.frame(data_tab_id)
#2.通过元素定位（xpath）来切换iframe
frame_id=driver.find_element_by_xpath("//iframe[@id='{}']".format(data_tab_id))
driver.switch_to.frame(frame_id)

#3.通过iframe的下标来切换

driver.find_element_by_id("searchNumber").send_keys("314")



driver.find_element_by_xpath("//span[@class='l-btn-left']//span").click()

time.sleep(2)

num =driver.find_element_by_id("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text

if '314' in num:
    print("搜索结果是正确的")
else:
    print("用例测试不通过")
time.sleep(5)
driver.quit()
