class test:

    a = 100

    def __init__(self, b, c):
        self.firstNumber = b
        self.secoundNumber = c
        print("defualt constructor")

    def demoMethod(self):
        print("method")
    
    
    def added(self):
        return self.firstNumber + self.secoundNumber + test.a

obj = test(2, 3)
obj.demoMethod()
print(obj.added())