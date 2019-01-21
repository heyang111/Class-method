# 类方法@classmethod
# 定义一个类
class Class_Method(object):
    num=18
    def __init__(self, name):
        self.name = name

    # @classmethod
    # def classmet(cls):
    #     print("i'm classmethod%s"%cls.num)
    """通过类方法能访问类变量，但必须在方法里传入一个参数cls，这个参数表示自身类，在调用类里的参数时用cls.xxxx
    """
    @classmethod
    def classmet(self):
        print("i'm classmethod%s"%self.name)

t = Class_Method("sddd")
t.classmet()

"""给类方法传入实例self，实例化一个类，传入name sddd,在调用类方法
   报错：AttributeError: type object 'Class_Method' has no attribute 'name'，类方法不能调用实例变量
"""


