class MyTime:
    '''Represents the time day.
        attributes: hours, minutes, and seconds.'''

    def __init__(self, hrs=0, mins=0, secs=0):
        total_seconds = hrs*3600 + mins*60 +secs
        self.hours = total_seconds // 3600
        leftoversecs = total_seconds % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        '''Returns a string represtation of the Time object.'''
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def to_seconds(self):
        '''Converts the Time object into seconds.'''
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        '''Overrides the addition operator to add two Time objects.'''
        if isinstance(other, MyTime):
            return MyTime(0, 0, self.to_seconds() + other.to_seconds())
        elif isinstance(other, int):
            return MyTime(0, 0, other + self.to_seconds())
        else:
            msg = f"MyTime doesn't know how to add type {type(other)}"
            raise TypeError(msg)

    def is_after(self, other):
        '''Returns True if this MyTime object is after the 
            other MyTime object'''
        return self.to_seconds() > other.to_seconds()

# hours minutes seconds base 60
# seconds – the ones place or 60^0
# minutes – the sixties place or 60^1
# hours – the thirty-six hundreds place or 60^2

def test():
    time1 = MyTime(2, 45, 45)
    print(time1)
    time2 = MyTime(4, 20, 15)
    print(time2)
    print(f"{time1} + {time2} = {time1 + time2}")
    print(f"{time1} + 12345 = {time1 + 12345}")
    if time1.is_after(time2):
        print(f"{time1} is after {time2}")
    else:
        print(f"{time2} is after {time1}")
        

if __name__ == '__main__':
    test()