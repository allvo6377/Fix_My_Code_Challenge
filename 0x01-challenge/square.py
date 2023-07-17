#!/usr/bin/python3
""" A module containing a square class. """


class Square():
    """Square class."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new square. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ area of square. """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ perimeter of square. """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string format of square. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
