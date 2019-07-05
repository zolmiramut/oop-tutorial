class Polygons:
    """
    provides a blue-print for the rest of the classes
    """

    def __init__(self):
        print("hi")
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rect(Polygons):
    def __init__(self, w, l):
        """
        takes the width and length of a rectangle and stores them in self
        :param w: width of the rectangle
        :param l: length of the rectangle
        """
        self.w = w
        self.l = l

    def area(self):
        """
        prints teh area of the rectangle

        :return: none
        """
        print(self.l * self.w)

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        :return: Area of a rectangle
        """
        return 2 * self.w + 2 * self.l


r1 = Rect(8, 9)
r1.area()
print(r1.perimeter())
