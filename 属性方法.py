# 通过@property把方法变成静态属性
class Property_method(object):
    def __init__(self,name):
        self.name=name

#     def Print_name(self):
#         print("My name is:%s"%self.name)
#
# t=Property_method("Jack Chen")
# t.Print_name()
    """正常调用Print_name要加括号
    """
    @property
    def Print_name(self):
        print("My name is:%s"%self.name)

t=Property_method("Jack Chen")
t.Print_name
"""用@property装饰方法后，调用方法加括号会报错:TypeError: 'NoneType' object is not callable,去掉括号后正常
   另外属性方法可以用.setter和.deleter修改删除
"""