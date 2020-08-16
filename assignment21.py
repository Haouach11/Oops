class Person:
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def my_function(self):
        print("My name is " + self.name)
        print("I am",end=' ')


p1 = Person("oussama", 18)
p1.my_function()
p1.age = 18
print(p1.age)






