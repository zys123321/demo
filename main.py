class Shape(object):
    @property
    def area(self):
        pass

class Ellipse(Shape):
    pi = 3.1415926
    def __init__(self,a=0,b=0):
        super().__init__()
        self.a=a
        self.b=b         
    @property
    def area(self):
        return self.a*self.b*self.pi        

class Circle(Ellipse):
    def __init__(self,r=0):
        super().__init__(r,r)         

class Rectangle(Shape):
    def __init__(self,width=0,height=0):
        super().__init__()
        self.width=width
        self.height=height         
    @property
    def area(self):
        return self.width*self.height         

class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)

shapes = [Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)] 

def computer__area(shapes):
    areas=[x.area for x in shapes]
    return sum(areas)

total__area=computer__area(shapes)
print('total_area: ',total__area)
