import math

# list of variable types allowed to assign as coordinates
TYPES_TO_FLOAT = [float, int]


# this class represents 3D vector (position or velocity vector)
class KinematicVector:
    def __init__(self, *args, **kwargs) -> None:
        """class' constructor
        :param *args: arbitrary positional arguments:
        - 0 parameters - () - create a (0,0,0) vector,
        - 1 parameter - (a) - create a (a,a,a) vector,
        - 3 parameters - (a,b,c) - create a (a,b,c) vector,
        :param **kwargs: arbitrary keyword arguments:
        - x = a - create a (a,~,~) vector,
        - y = b - create a (~,b,~) vector,
        - z = c - create a (~,~,c) vector,
        :return: None"""
        self.x = float(0.0)
        self.y = float(0.0)
        self.z = float(0.0)
        if args:
            match len(args):
                case 1:
                    if type(args[0]) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(args[0])}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    self.x = float(args[0])
                    self.y = float(args[0])
                    self.z = float(args[0])
                case 3:
                    if type(args[0]) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(args[0])}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    if type(args[1]) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(args[1])}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    if type(args[2]) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(args[2])}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    self.x = float(args[0])
                    self.y = float(args[1])
                    self.z = float(args[2])
                case _:
                    raise Exception(f"You can use 0, 1 or 3 arbitrary arguments, but there is {str(len(args))}")
        if kwargs:
            for key, value in kwargs.items():
                if key == "x":
                    if type(value) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(value)}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    self.x = float(value)
                    continue
                if key == "y":
                    if type(value) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(value)}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    self.y = float(value)
                    continue
                if key == "z":
                    if type(value) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(value)}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    self.z = float(value)
                    continue
                raise Exception(f"Incorrect keyword argument: {str(key)}")

    def __repr__(self):
        """function returning a string representation of the vector
        :return: a string representation of the vector"""
        return f"[x = {self.x:.8f}, y = {self.y:.8f}, z = {self.z:.8f}]"

    def length(self):
        """function returning the length of the vector
        :return: length of the vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def check_types(self):
        """function checking the types of the coordinates - if they
        are different then float, they can be changed if possible.
        The adequate communicates are displayed by the console.
        :return: None"""
        if type(self.x) != float:
            self.x = float(self.x)
            print("x-coordinate changed to float")
        if type(self.y) != float:
            self.y = float(self.y)
            print("y-coordinate changed to float")
        if type(self.z) != float:
            self.z = float(self.z)
            print("z-coordinate changed to float")
