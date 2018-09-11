class Student():
    def __init__(self,name="小明",age=18):
        self.name= name
        self.age = age
    def say(self):
        print("My name is {0}".format(self.name))
def Sayhello():
    print("hello world")
print("this is p01 module")