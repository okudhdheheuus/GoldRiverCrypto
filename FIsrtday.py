
N=2
# 一、python数据类型与变量
def print_datastr():
    # 在下面的代码行中使用断点来调试脚本。
    print('data structure test')  # 按 Ctrl+F8 切换断点。
    # 1.List列表
    weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    print(weekday[0]) # 输出Monday
    #list搜索
    print(weekday.index("Wednesday"))
    #list增加元素
    weekday.append('new')
    print(weekday)
    #lsit删除
    weekday.remove("Thursday")
    print(weekday)
    # 2.Tuple元组
    letters = ('a','b','c','d','e','f','g','h')
    print(letters[0]) #输出'a'
    print(letters[0:3]) #输出一组（‘a','b','c'） 0:3表示0<=i<3
    # 3.Sets(集合) 无序不重复元素的序列，使用{}或者set()函数创建集合，创建空集合必须用set()而不是{}，因为{}是用来创建一个空字典
    # 集合不能被切片也不能被索引，除了做集合运算外，集合还可以被添加还有删除
    a_set = {1,2,3,4}
    #添加
    a_set.add(5)
    print(a_set)
    #删除
    a_set.discard(5)
    print(a_set)
    # 4.Dictionary(字典) 类似java map 集合接口 字典是一种映射类型，它的元素是键值对，字典的关键字必须为不可变类型，且不能重复。空字典用{}
    Logo_code = {
        'BIDU':'BaiDu',
        'SINA':'Sina',
        'YOKO':'YouKu'
    }
    print(Logo_code)
    print(Logo_code['SINA']) #输出键为‘SINA’的值
    print(Logo_code.keys()) #输出所有键
    print(Logo_code.values()) #输出所有值
    print(len(Logo_code)) #输出字段长度
    # 5.String(字符串)
    s='学习Python'
    #切片
    print(s[1])  # 打印"习"
    print(s[-1])    # 'n'
    print(s[3:])    # 打印‘ython’
    print(s[::-1])  #逆向按步长为-1打印
    #查找，可以使用正则表达式替换
    t=s.replace('Python','Java') # ‘学习Java’，不修改原值,修改结果以返回值形式保存
    print(t)
    # 查找，find()、index()、rfind()、rindex()
    print(s.find('P'))  #返回第一次出现的字串的下标
    print(s.find('t',0,4)) #设定下标查找,找0.1.2.3，没有返回-1
    print(s.index('y')) #返回第一次出现值下标，没有抛出异常
    # 转换大小写，upper()、lower()、swapcase()、isupper()
    print(s.upper()) #返回大写形式
    print(s.swapcase())  ##返回大小写转换后结果
    print(s.title()) #转换首字母为大写，其余为小写
    print(s.islower()) #判断是否小写形式，返回false
    # 连接与分割，使用+连接字符串，每次操作会重新计算、开辟、释放内存，效率低下,适合使用join
    l = ['2017', '03', '29', '22:00']
    s5 = '-'.join(l)  # 返回一个每个子串之间增加'-'分隔组成的大串
    print(s5)
    s6 = s5.split('-') # 返回一个以‘-’为分割符拆解大串s5后得到的字串组
    print(s6)
    # 6.变量
    a= b = c = 1  #同时为多个变量赋值
    a,b,c = 1,2,3 #依次赋值
    AI = 5 # 变量名全部大写表示定义一个常量（通用表示），AI值是可以改变的
    AI = 1
    print(AI)

 # 二、 控制流
def print_contr():
    print('control flow test')
    # 1.if语句
    a = int(input('输入一个数字：')) # 使用input函数提示输入语句后，获得用户输入字符串，并通过（int）强转为对应数据类型， if语句块结构为if,elif,else,elif可以表示多种不同情况
    if a<0:
        print('a是负数')
    elif a==0:
        print('a等于0')
    else:
        print("a为正数")
    # 2.while语句
    while a:
        a=a-1
        if a==0: break
        print(a)
    else:            ##相比于c语言while语句，多了一个else语句，当循环正常执行到条件不满足退出时执行一次else，如果是break退出的循环则不执行
        print('a的值已经为：',a)
    # 3.for循环
    l = ['a','b','c']
    for i in l:     #基本格式为 for + 下标计量 + in + 队列
        print(i)
    else:              #与while的else作用类似
        print('the for loop is over')
    print('d',N)


# 三、函数
# 定义形式为 def+函数名+（参数名）+':'
def dfpar_ts(a,b=5,c=10):
    print('a is',a,'b is',b,'c is',c)
def varargs_ts(a=5,*numbers,**phonebook):
    print('a',a)            #默认值为5，如若需要传入一个元组给numbers，而没有特定给a传值，则会自动把第一个数字传给a，需要额外给a一个数值
    for item in numbers:    #对于第二个参数表示从此处开始到结束传入的所有值收集成一个名为numbers的元组
        print('sigle_item is',item)
    for item1,item2 in phonebook.items(): #第三个参数表示从某处开始的所有连续的形如‘Jack’='10'的关键字参数收集成一个字典
        print(item1,item2)


def print_func():
    print('function test:')
    # 1.global语句
    # 这里程序最上层定义了一个变量N=2，如果不用global，则对N值的改变只会作用于本代码块中，包括子块（本块调用的函数快等）
    global N        #此语句之前不能使用全局变量N，且global语句作用是赋予本代码块对最上面本变量进行远程改变的权力
    N=1
    print('f',N)     # ‘1’
    # 2.默认参数值
    # 假定定义一个函数形式为def say(message,times=2),这里的‘=2’就表示times的默认值为2及如果传参时只传一个值则默认time值为2
    # 注意函数参数列表中没有默认值的的参数必须放在有默认值参数之前
    # 3.关键字参数
    # 在传参时通过命名对指定参数传值，而不需要刻意保证参数顺序，且保证只对特定参数传值，其他参数保持默认值
    #这里定义了一个def dfpar_ts(a,b=5,c=10):的函数 分别打印a,b,c的值
    dfpar_ts(25,c=24)    #b默认
    dfpar_ts(1)             #b,c默认
    # 4.可变参数
    # 让参数数量可变 这里定义了一个形如def varargs_ts(a=5,*numbers,**phonebook):的函数，分别打印这里组成的单值，元组，字典
    print(varargs_ts(5,3,4,Lucy='女',John='男',Bob='男'))#其中3,4组成一个元组，最后三个值组成一个字典，键为名字，值为性别
    # 5.return语句
    ''' 用于中断函数并返回一个值，不特别写return语句则默认返回none,就像下面这段代码
    def some_fuc():
        pass  
    这里的pass语句用于指定一个没有内容的语句块 '''
    # 6.DocStrings
    #






#临时测试
def test():
    print('test')
# 按装订区域中的绿色按钮以运行脚本。

if __name__ == '__main__':
    #print_datastr()
    #print_contr()
    print_func()

