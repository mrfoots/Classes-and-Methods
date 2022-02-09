class Point:
    '''Represents a point in 2-D space.
        attributes: x, y
    '''
    def __init__(self, x=0, y=0):
        '''Initializes a new Point object with default attributes.'''
        self.x = x
        self.y = y

    def __str__(self):
        '''Returns a string representation of a Point object.'''
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        '''Overloads the + operator to add two Point or a Point and a tuple.'''
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            msg = f"Point doesn't know how to add type {type(other)}"
            raise TypeError(msg)        

    def distance_from(self, other=(0, 0)):
        '''Returns the distance between this Point object and another Point object.'''
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        elif isinstance(other, tuple):
            return ((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2) ** 0.5

    def halfway_to(self, target):
        '''Returns a new Point object that is located between this Point object 
            and a target Point object.'''
        mid_x = (self.x + target.x)/2
        mid_y = (self.y + target.y)/2
        return Point(mid_x, mid_y)


def test():
    p1 = Point(2, 4)
    p2 = Point(7, 8)
    print(f"p1 is {p1}.")
    print(f"p2 is {p2}.")
    print(f"p1 + p2 is {p1 + p2}.")
    print(f"p1 + (3, 4) is {p1 + (3, 4)}.")
    print(f"The distance between {p1} and {p2} is {p1.distance_from(p2)}.")
    print(f"The point {p1.halfway_to(p2)} is the mid point between {p1} and {p2}.")

if __name__ == '__main__':
    test()