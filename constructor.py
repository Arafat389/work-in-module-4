#  __init__(self)  constructor

class myclass:
    def __init__(self):   # apna apnami execution hoi
                           # ati return kora jai na
        print("I am a constructor")


obj = myclass()  



# constructor without parameter

class myclass:

    a = 20
    b = 10
    def __init__(self):   # apna apnami execution hoi
         sum = self.a + self.b                  # ati return kora jai na
         print(sum)


obj = myclass() 


# constructor with parameter

class myclass:

    a = 20
    b = 10
    def __init__(self,x,y):   # apna apnami execution hoi
         sum = self.a + self.b+x+y                 # ati return kora jai na
         print(sum)


obj = myclass(30,40) 