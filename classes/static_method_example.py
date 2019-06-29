import util_module


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def show_info(self):
        print(self.ingredients, '\n', self.radius)

    def area(self):
        return util_module.circle_area(self.radius)

    # @staticmethod
    # utility function
    # def circle_area(r):
    #    return r ** 2 * math.pi


p = Pizza(5, ['chicken', 'cheese'])
print("area : ", p.area())
print("Info : \n")
p.show_info()
