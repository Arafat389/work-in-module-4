# father ase child nai

"""
class father:
    a = 10
    b = 20
    def add(self):
        print(self.a + self.b)

    def __init__(self):
        print("father constractor")    

class son(father):
    pass

obj = son()
obj = father()

"""

"""

# father nai child ase

class father:
    a = 10
    b = 20
    def add(self):
        print(self.a + self.b)

        

class son(father):
    def __init__(self):
        print("son constractor")

obj = son()
obj = father()


"""
"""

# father nai child ase

class father:
    a = 10
    b = 20
    def add(self):
        print(self.a + self.b)
    def __init__(self):
        print("father constractor")
        

class son(father):
    def __init__(self):
        print("son constractor")

obj = son()
obj = father()


"""


# child ase taw child baber ta kibabe access kore


class father:
    a = 10
    b = 20
    def add(self):
        print(self.a + self.b)
    def __init__(self):
        print("father constractor")
        

class son(father):
    def __init__(self):
        super().__init__()
        print("son constractor")

obj = son()
obj = father()