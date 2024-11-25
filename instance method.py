class myclass:
    a = 10
    b = 20
    # c= 100
    def __init__(self,cvalue,avalue):
        self.c = cvalue
        self.a = avalue

    def addtwo(self):
        s = self.a+self.b+self.c
        print(s)
obj = myclass(100,5)
print(obj.c)
print(obj.a)
obj.addtwo()

