class Student():
    def __init__(self,name="小明",age=18):
        self.name= name
        self.age = age
    def say(self):
        print("My name is {0}".format(self.name))
def Sayhello():
    print("hello world")
print("this is p01 module")
#下面这行这句话作为以后所有编程入口
if __name__ == "__main__":
    print("主线程专属")