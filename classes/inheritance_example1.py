class Bird:  # parent class
    message = 'hello0000000000000000000000'  # puplic variable
    canfly = ' Can Fly '
    cannotfly = ' Can not Fly '


def intro(self):
    print("There are many types of birds.")


def flight(self):
    print("Most of the birds can fly but some cannot.")


class sparrow(Bird):  # child 1
    # method overriding
    def flight(self):
        print("Sparrows" + Bird.canfly + Bird.message)


class ostrich(Bird):  # child 2
    # method overriding
    def flight(self):
        print("Ostriches" + Bird.cannotfly + Bird.message)


obj_spr = sparrow()
obj_ost = ostrich()

# Polymorphism
obj_spr.flight()
obj_ost.flight()
