# single  parients

"""
class father:
    a = 10
    b = 20
    def addtwo(self):
        s = self.a + self.b
        print(s)

    def multwo (self):
        s = self.a * self.b
        print(s)


class son(father):
    pass

obj = son()
obj.addtwo()
obj.multwo()
print(obj.a)
print(obj.b)


obj = father()
obj.addtwo()
obj.multwo()
print(obj.a)
print(obj.b)

"""


# multiple parients

"""

class father:
    a = 10
    b = 20
    def addtwo(self):
        s = self.a + self.b
        print(s)

    def multwo (self):
        s = self.a * self.b
        print(s)

class mother:
    a = 100
    b = 20
    def subtwo(self):
        s = self.a - self.b
        print(s)

    def divtwo (self):
        s = self.a / self.b
        print(s)

class son(father):
    pass

obj = son()
obj.addtwo()
obj.multwo()
print(obj.a)
print(obj.b)


obj = father()
obj.addtwo()
obj.multwo()
print(obj.a)
print(obj.b)


obj = mother()
obj.subtwo()
obj.divtwo()
print(obj.a)
print(obj.b)

"""
"""

class father:
    a = 10
    b = 20
    def addtwo(self):
        s = self.a + self.b
        print(s)

    def multwo (self):
        s = self.a * self.b
        print(s)

class mother:
    x = 100
    y = 20
    def subtwo(self):
        s = self.x - self.y
        print(s)

    def divtwo (self):
        s = self.a / self.b
        print(s)

class son(father,mother):
    pass
#father
obj = son()
obj.addtwo()
obj.multwo()
print(obj.a)
print(obj.b)
#mother
obj.subtwo()
obj.divtwo()
print(obj.x)
print(obj.y)

"""

# multilebel

class grandfather:
    a = 10
    b = 20
    def addtwo(self):
        s = self.a + self.b
        print(s)

    def multwo (self):
        s = self.a * self.b
        print(s)

class father(grandfather):
    pass
class son(father):
    pass

obj = son()
obj.addtwo()






