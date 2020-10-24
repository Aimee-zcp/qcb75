"""

for 循环：遍历对象 数据对象里的所有元素：str，list，tuple，dict，集合

    for 变量名 in 数据对象
        子代码（循环体）
    循环多少次是由元素个数决定的。
中断：
   break --跳出循环
   continue ---结束当前循环，本次循环该语句后面的语句不执行
   range() --内置函数:生成一个整数序列：1，2，3，4，5，6
            跟for循环一起使用,start开始，stop结束，step步长--取头不取尾
           eg: for i in range(1,5,1):
                print(i)
count=0
list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Aimee', '焕蓝']
for name in list1:
    if name=="Aimee":
        break  # 跳出循环
    print(name)
    print("*"*20)
    count+=1
print(count)
print(len(list1))

函数： 经常需要使用的代码块封装成函数，便于调用，==提高代码的复用率，提高执行效率
 语法：
  def 函数名():  ---标识符，必须满足标识符的规则
        子代码(函数体) ---实现功能
 注意：函数只定义了  没有调用是不会执行的。--如何调用？ 直接写函数名

 函数里不固定的数据---定义成函数的参数--扩号里
 1.形参：函数定义的时候 定义的
 2.实参：调用函数传入参数
 参数定义的类型：--形参
    1.必备参数：定义了就必须要传入的参数--不传会报错
    2.默认参数（缺省参数）：可以定义的时候赋值一个默认值---调用的时候可以不传；可以传--替换掉默认值
    注意：默认参数必须在必备参数后面！！
    3.不定长参数：等前面的必备参数和默认参数都接收完了，剩下的都给不定长参数接收
       *args:接收不确定数量，个数的参数--可以不传，可以传入（1个，多个）==元祖接受
    注意：不定长参数一半放在参数的末尾
    4.**kwargs:用字典接收，不定长度
    good_job(9000,bouns=2000,subsidy=2000,aa=50,bb=200,cc=800,dd=300)
传参的方式：
1.位置传惨：按照参数的位置传入参数
2.关键值传参：指定参数名来进行传参，不关心顺序--可靠
3.关键字传参必须跟在位置参数的后面
good_job(9000,bonus=2000,subsidy=2000)
"""


def good_job(salary,bouns,subsidy=500,*args,**kwargs):#定义--函数名===函数参数===形参-变量替代，
    sum1=salary+bouns+subsidy
    print("args的值是：{}".format(args))
    print("这个工作的工资总和是{}".format(sum1))
    print("args的值是{}".format(args))
    for i in args:
        sum1 +=i
    for j in kwargs:
        print(kwargs.get(j))
        sum1 +=kwargs[j]
    print("kwargs的值是{}".format(kwargs))
    return sum1,salary
# good_job(9000,bouns=2000,subsidy=2000,aa=50,bb=200,cc=800,dd=300) # 用函数名进行函数的调用---函数才会被执行
# good_job(8000,2000,500,100,200,300,aa=50,bb=200,cc=800,dd=300)#100,200,300是传给args的变长参数，后面的是

"""
有进有出： 进--参数，出--返回值
返回值：函数可以给到外面的人用的数据--调用函数的时候，可以获取到这个返回值做后续的操作--return
1.定义
2.调用
3.如果没有返回值，那么返回None，可以有return:---可以多个：return sum1，salary ----多个返回值用逗号隔开，---元祖保存
4.注意：返回值写在函数的最后---标志着函数的结束----return之后的代码不会在执行
"""
# result=good_job(8000,2000,500,100,200,300,aa=50,bb=200,cc=800,dd=300)
# print(result)

"""
内置函数：
 print
 input() ---输入的都是字符串
 type
 isinstance
 count
 len()
 replace find index append insert pop remove.......---数据类型的内置方法
 str float int() list() tuple() dict() ,bool() set()
 rang()---整数序列
"""


# 1. 把字符串转成列表 - list()
# str1="2name胖妞"
# print(list(str1))

def strToList(str1):
    return list(str1)

str2="2name胖妞"
list1=strToList(str2)
# print(list1)


# 2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
def addFunction(num):
    sum1=0
    for a in range(1,num):
        sum1 +=a
    return sum1

# number=int(input("请输入一个整数："))
# result=addFunction(number)
# print("整数序列相加的结果是：{}".format(result))

# 3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
def xiaoxingxing(object):
     type1=type(object)
     if type1 in (list,dict,str):
         if len(object)>5:
             return True
         else:
             return False
     else:
         return "type not in (list,dict,str)"

xixixi=32
result=xiaoxingxing(xixixi)
print(result)
