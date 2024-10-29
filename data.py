import math
from typing import Any


# Representation of time as hours, minutes, and seconds
class Time:
    # Initialize a new Point object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    '''this function is a property of the Time class that dictates what must be equal about two 
    Time objects in order for them to be considered equal. It inputs 2 Times and outputs a bool.
    '''
    def __eq__(self, other:Any):
        if ((type(other) == Time) and (other.hour == self.hour) and
                (other.minute == self.minute) and (other.second == self.second)):
            return True
        else:
            return False


    # Provide a developer-friendly string representation of the object.
    # input: Time for which a string representation is desired. 
    # output: string representation
    '''This function is a property of the Time function and dictates what is returned when a bit 
    of code tries to print a Time. It inputs a Time and outputs a string. 
    '''
    def __repr__(self):
        return ("Hour: {}, Minute: {}, Second: {}"
                .format(str(self.hour), str(self.minute), str(self.second)))


    # Compare the Time object with another value to determine equality.
    # input: Time against which to compare
    # input: Another value to compare to the Time
    # output: boolean indicating equality




# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other:Any) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
