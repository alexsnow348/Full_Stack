class Parent(object):
    """docstring for Parent."""
    def __init__(self, last_name,eye_color):
        super(Parent, self).__init__()
        print("Parent Constructor called.")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last Name - ", self.last_name)
        print("Eye Color - ", self.eye_color)

class Child(Parent):
    """docstring for Child."""
    def __init__(self, last_name,eye_color,number_of_toys):
        print("Child Constructor called.")
        # Parent.__init__(self,last_name,eye_color)
        super(Child,self).__init__(last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - ", self.last_name)
        print("Eye Color - ", self.eye_color)
        print("Number of Toys - ", self.number_of_toys)
