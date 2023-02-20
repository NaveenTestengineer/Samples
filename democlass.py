class root:
    a = 100


    def __init__(self, b, c):
        print("constructor executed")
        
    
    def user(self):
        print("a iam executing")

    
    def sum(self):
        self.firstNumber = b
        self.secoundNumber = c
        print("firstnumber+secoundnumber")

nav = root(2, 3)
nav.user()
print(nav.a)     
print(nav.sum())