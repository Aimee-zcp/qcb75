from idlelib.search import find

# print 可以作为表示符，但是不建议，内置函数的名字，--因为一旦使用了，这个函数就不能用了
"""
变量：存储数据的
    数据类型： int float，bool，str
变量名定义规则：标识符1，2，3，4
5.见名知意：
6.变量名一定要先申明（定义并赋值），再调用，否则会报错


字符串的操作：
 1.取值：位置--索引，从0开始，依次加1
 2.取多个值：将字符串切片---[开始:结束:步长]====取头不取尾
 开始头--省略==默认从0开始
 结束--省略===默认末尾结束
 步长--省略===默认为1
 3.负数：从右边开始取  -1---最后一个
 4.元素个数：len()---内置函数：统计元素个数(长度)
 5.替换字符串里的元素：replace()
 6.查找元素位置：index() 查不到的时候报错，代码会终止运行
                find() 如果元素没有找到，--不会报错，返回-1
 7.count  统计
 
 格式化输出：
   第一种： .format()
    1.使用占位符{},传变量的地方，再用.format()方法传入参数
    2 .format()可以默认位置传入参数，也可以指定位置传入变量==注意：不能混合使用
    name="Aimee"
    age=18
    hobby="学习"
    print(\"""
    ----{0}----
    name:{1}
    age:{2}
    hobby:{3}
    \""".format(name,name,age,hobby))
  第二种：%s --字符串（可以匹配所有的类型） %d --传整数  %f  --传小数  ----必须按照位置严格传入参数
            不确定的时候用%s匹配所有类型
   name="Aimee"
    age=18
    hobby="学习"
    print(\"""
    ----%s----
    name:%s
    age:%d
    hobby:%s
    \"""%(name,name,age,hobby))
    Python运算符：
     1.算术运算符：+ - * / % **
      加法:数字相加，字符串拼接
        print(str(135)+"abd")
      减法： 数字相减 print(20-10)
       int--->str:str() ---强制字符串的转化
       int()强制转化为int
       float() 强制转化为float
     乘法：两个数字相乘，字符串*数字表示将字符串重复输出
     除法：print(10/3) # 结果是浮点型
     取幂：两个**表示
 2.赋值运算符：= ，+=，-=  ：方向性---右边的值赋值给左边
   a=10
   a+=10 ===表示a=a+10
   a-=5 ===表示a=a-5
 3.比较运算符： <, >, = ,>=, <= ,!=  ----运算结果是布尔值:True,False
   print("登录成功"=="登录成功") #判断字符串是否相同===执行结果 VS预期结果
 4.逻辑运算符： 与 -and  真真为真，或 -or 假假为假  非 -not  
    print(2>3 and 3<4)--- False
    print(not 2>3) 返回 True
 5.成员运算符： in，not in ---判断子字符串是否在源字符串中
     str2="python"
     print("p" in str2)   
  
  7.屏幕输入函数：input()
      num=input() 内置函数，获取控制台的输入 ，然后将输入赋值给num
     
"#作业1
# name=input("请输入姓名：")
# age=input("请输入年龄：")
# sex=input("请输入性别：")
#
# print('*'*30)
# print(
#     """
#     姓名：{}
#     年龄：{}
#     性别：{}
#     """.format(name,age,sex))""
# print('*'*30)


#作业2
str1="python hello aaa 123123aabb"
#1.请取出并打印字符串中的"python"
str2="python"
print(str1[0:len(str2)])
#2.请分别判断'o a' 'he' 'ab'是否是改字符串中的成员？
print("o a" in str1)
print("he" in str1)
print("ab" in str1)

print("o a" not in str1)
print("he" not in str1)
print("ab" not in str1)
#3.替换python为"lemon"
print(str1.replace("python","lemon"))
#4.找到aaa的起始位置:
print(str1.index("aaa"))