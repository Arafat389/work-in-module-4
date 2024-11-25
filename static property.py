#  use static method

class myclass:
    a = 10 
    b = 20
# def addtwo (self): not staticmethod

    @staticmethod
    def addtwo():  # staticmethod
        s = myclass.a + myclass.b   # self not allow use main class (myclass)
        print(s)

myclass.addtwo()  # direct call class not object     

# not use staticmethod 
# only object

obj = myclass()
obj.addtwo()


#  use static variable

class myclass:
    a = 10 
    b = 20

print(myclass.a)
print(myclass.b)  

obj = myclass()
print(obj.a)


