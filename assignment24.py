class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


Circle1 = Circle(int(input("enter a value: ")))
print("the area is: " , Circle1.area())
print("the perimeter is: " , Circle1.perimeter())
