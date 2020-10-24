
"""
常用的数据类型：列表（list），元祖（），字典（），集合（）
列表（list）:[],
list1=[]  #可以定义一个空列表
1.元素可以是任意的数据类型：int，float，bool str list...
2.元素之间用英文的逗号隔开
  取值：索引取值---类比字符串
    取多个值：切片
    扩展：列表嵌套取值
 3.列表的元素是可以被改变的！--增加，修改，删除
  #增加
    insert---用于指定位置进行元素的插入
    eg:list1.insert(5,"Aimee")
    extend（）--用于批量添加
     eg:list1.extend(['小胖妞','大牛','黑娃','天天'])
 #删除
    list1.pop() #默认删除最后一个元素，也可以指定索引进行删除
    list1.remove(3.14) #指定元素进行删除
    list1.clear()#清除所有元素
 4.列表元素可以重复----统计个数---count
 5.len() ---长度
"""
# list1=[20,3.14,True,"荷花鱼","桤木",[1,2,3,4]]  #可以定义一个空列表
# print(list1[5][0])
# list1.insert(5,"Aimee")
# list1.extend(['小胖妞','大牛','黑娃','天天'])
# print(list1)
#
# #删除
# list1.pop() #默认删除最后一个元素，也可以指定索引进行删除
# list1.remove(3.14) #指定元素进行删除
# #list1.clear()#清除所有元素
# print(list1)
#
# #修改
# list1[4]="憨憨"
# print(list1)
# list1.append("Aimee")
# print(list1)
# print(list1.count("Aimee"))

"""
元祖： tuple,元素用()括起来
1.元素可以是任意的数据类型：int，float，bool str list，tuple...
2.元素之间用英文的逗号隔开
  取值：索引取值---类比字符串
    取多个值：切片
    扩展：列表嵌套取值
 3.元祖的元素是不可以被改变的
    若是想要改变，先将元祖强转为列表，改变之后再转换回去
 4.列表元素可以重复----统计个数---count
 5.len() ---长度
 6.list(),tuple()---扩展：数据类型转换
"""
# tuple1=(20, True, '荷花鱼', '桤木', '憨憨', [1, 2, 3, 4], '小胖妞', '大牛', '黑娃', 'Aimee')
# # print(len(tuple1))
# # list2=list(tuple1)
# # list2[-2]="黑莓"
# # print(list2)
# # tuple2=tuple(list2)
# # print(tuple2)
"""
字典：dict {}
 1.元素: key,value---键值对
 dict1={"name":"tan","height":"190","weight":"80kg"}
 dict2=dict(name="Aimee",age=18,hobby="cooking")
 2.场景：存储数据属性：人--名字 身高 体重
    key:1）不能是可以改变的数据类型（list，dict）---字符串
        2）不能重复的，唯一的
    value：可以是任意数据类型
 3.字典是没有顺序的！！---不能用索引取值，取值：get()
   获取:
   dict1["height"]
   dict1.get("name")
   新增
    dict1["age"]=18  #如果这个key不存在，则新增键值对  
 删除 需要指定key值进行弹出，因为字典是没有顺序的。
 del dict1 #删除变量--变量对象都已经被删除了
 4.取长度--len()
 5.批量增加：---相当于两个字典合并---update时若key已经存在则更新
    dict1.update({"city":"北京","hobby":"学习看书"})

集合：set {}，元素单个，
1.无序
2.元素不可以重复--使用场景：去重---转换成集合去重之后再转换回去
list2=[12,123.25,11,25,13]
set1=set(list2) #set()  --list2转化为集合
 list3=list(set1) #list() --set1 转化为列表
"""
# dict1={"name":"tan","height":"190","weight":"80kg"}
# print(dict1["height"])
# print(dict1.get("name"))
# dict1["height"]="180"
# print(dict1)
# dict1.setdefault("hobby","cooking")
# dict1["age"]=18  #如果这个key不存在，则新增键值对
# dict1.pop("hobby")
# print(dict1)
#
# dict1.update({"city":"北京","hobby":"学习看书"})
# print(dict1)

"""
控制流:代码的执行的顺序--从上至下依次执行： 判断，循环
判断：if 语法
 if 条件： --成立--冒号：缩进(四个空格=tab键)
    子代码(执行语言)
 elif 条件：---成立
    执行语句（子代码）
 ...(elif可以没有，可以有多个)
 else：---可以没有
    执行语句（子代码）
     
"""
# money=500100
# if money>=500:
#     print("买车")
# elif money>4000:
#     print("买别墅吧")
# elif money<100:
#     print("钱不够")
# else:
#     print("你太有钱了呀！！！！")
# dict2=dict(name="Aimee",age=18,hobby="cooking")
# print(dict2)

#1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面

# a=[1,2,'6','summer']
# print("i" in a)

# 2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
# 注：num表示课堂人数。如果大于5，输出人数
# dict_1={"class_id":45,'num':20}
# num=dict_1.get("num")
# if num>5:
#     print(dict_1["num"])

# 3、list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
# 并且把字典都存在新的 list中，最后打印最终的列表。
# 方法1： 手动扩充--字典--存放在列表里面；
# 方法2： 自动--dict（）

#方法1： 手动扩充--字典--存放在列表里面；
# list2=[]
# list3=[]
# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
#
# dict1={"name":list1[0],"gender":"male","age":22,"city":"天津"}
# dict2={"name":list1[1],"gender":"female","age":18,"city":"长沙"}
# dict3={"name":list1[2],"gender":"male","age":30,"city":"武汉"}
# dict4={"name":list1[3],"gender":"female","age":20,"city":"重庆"}
# dict5={"name":list1[4],"gender":"female","age":21,"city":"成都"}
# dict6={"name":list1[5],"gender":"male","age":25,"city":"南京"}
#
# list2.append(dict1)
# list2.append(dict4)
# list2.append(dict5)
# list2.append(dict6)
#
# list3.append(dict2)
# list3.append(dict3)
#
# list2.extend(list3)
# print(list2)

# 3、list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
# 并且把字典都存在新的 list中，最后打印最终的列表。
# 方法2： 自动--dict（）

list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
list2=[]
for index in range(len(list1)):
    list2.append(dict(name=list1[index],gender="female",age="18",city="成都"))

for index in range(len(list2)):
    print(list2[index])
