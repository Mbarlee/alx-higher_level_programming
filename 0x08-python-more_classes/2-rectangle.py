

#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """Rectangle definition"""
    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width validation and setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 is True:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height validation and setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0 is True:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__height is 0 or self.__height is 0:
            return 0
        return (2 * (self.__height + self.__width))
