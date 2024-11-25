"""
class myclass:
    a = 20
    b = 30
    c = 40
    s = a+b+c
    def addThree (self):
        sum = self.a + self.b + self. c
        print(sum)

obj1 = myclass() 
print(obj1.s)  

obj1.addThree()


class myclass:
    a = 20
    b = 30
    c = 40
    s = a+b+c
    def addThree (self,x,y,z):
        sum = self.a + self.b + self. c+x+y+z
        print(sum)

obj1 = myclass() 
print(obj1.s)  

obj1.addThree(20,30,50)

"""


# class bitore function/method then method method call kora
class myclass:
    a = 20
    b = 30
    c = 40
    s = a+b+c
    def addThree (self,x,y,z):
        sum = self.a + self.b + self. c+x+y+z
        print(sum)

    def addtwo(self):
        self.addThree(5,6,7)    

obj1 = myclass() 
print(obj1.s)  

obj1.addThree(20,30,50)
obj1.addtwo()
