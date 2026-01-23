class rectangle():
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    @property
    def cv (self):
        return (self.x + self.y) * 2
    @property
    def V (self):
        return self.x * self.y

x = int(input("x"))
y = int(input("y"))
sth = rectangle(x,y)
print(f"chu vi la:{sth.cv}")
print(f"dien tich la: {sth.V}")

