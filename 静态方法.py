# 实例方法和静态方法@staticmethod
# 定义一个类
class Static_Class(object):
    num=18
    def __init__(self, name):
        self.name = name

    # @staticmethod
    # def static(age):
    #     print("i'm staticmethod%s"%age)
    """不能访问类变量和实例变量
    """
#     @staticmethod
#     def static(num):
#         print("i'm staticmethod:%s"%num)
#
# Static_Class.static(100)
    """可以用类调用时传入参数
    """


    @staticmethod
    def static():
        print("i'm staticmethod")

Static_Class.static()
"""用@staticmethod装饰类里的方法可以不用把类实例化，直接用类调用，静态方法也不可以访问实例变量或类变量
"""

