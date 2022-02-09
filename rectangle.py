from point import Point

class Rectangle:
    '''Represents a 2-D rectangle object
        attributes: width, height, corner'''

    def __init__(self, width, height, location=(0,0)):
        '''Initializes a new Rectangle object with attribute values.
            width: integer value for the width attribute
            height: integer value for the height attribute
            location: tuple value with elements for x and y 
                used to create a new Point object for the corner attribute
        '''
        self.width = width
        self.height = height
        self.corner = Point(*location)

    def __str__(self):
        '''Returns a string represtnation of a Rectangle object
            displaying the width, height, and corner location.
        '''
        return f"Rectangle: width {self.width}, height {self.height}, located at {self.corner}."


    def resize_to(self, dwidth, dheight):
        '''Adjusts the width and height of the current Rectangle object'''
        self.width += dwidth
        self.height += dheight

    def move_to(self, x, y):
        '''Relocates the corner Point object of the Rectangle object
            to a new location.
        '''
        self.corner.x = x
        self.corner.y = y

    def move(self, dx, dy):
        '''Moves a Rectangle object.'''
        self.corner.x += dx
        self.corner.y += dy
        

def test():
    '''Creates a few example Rectangle objects, displays them, and calls their methods.'''
    rect1 = Rectangle(100, 50, (10, 10))
    rect2 = Rectangle(50, 150, (200, 100))
    print(rect1)
    print(rect2)
    rect1.resize_to(50, 50)
    rect1.move_to(20, 30)
    rect2.resize_to(50, 25)
    rect2.move_to(150, 125)
    print(rect1)
    print(rect2)

if __name__ == '__main__':
    test() # calls the test function only if this module is run directly