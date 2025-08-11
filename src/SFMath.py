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

    def __repr__(self) -> str:
        """method returning a string representation of the vector
        :return: a string representation of the vector"""
        return f"[x = {self.x:.8f}, y = {self.y:.8f}, z = {self.z:.8f}]"

    def length(self) -> float:
        """method returning the length of the vector
        :return: length of the vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def check_types(self) -> None:
        """method checking the types of the coordinates - if they
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

    def __neg__(self) -> 'KinematicVector':
        """method inverting a vector
        :return: inverted vector"""
        return KinematicVector(-self.x, -self.y, -self.z)

    def __abs__(self) -> float:
        """method returning a vector's length
        :return: vector's length"""
        return self.length()

    def __add__(self, other) -> 'KinematicVector':
        """method summing two vectors
        :param other: second vector to add
        :return: sum of the vectors"""
        if type(other) != KinematicVector:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        return KinematicVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other) -> 'KinematicVector':
        """method subtracting two vectors
        :param other: second vector to subtract
        :return: difference of the vectors"""
        if type(other) != KinematicVector:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        return KinematicVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other) -> 'KinematicVector':
        """method multiplying scalar and a vector
        :param other: number to multiply
        :return: vectors multiplied by the scalar"""
        if type(other) not in TYPES_TO_FLOAT:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        return KinematicVector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other) -> 'KinematicVector':
        """method dividing vector by a scalar
        :param other: number to divide
        :return: vectors multiplied by the scalar"""
        if type(other) not in TYPES_TO_FLOAT:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        if other == 0:
            raise Exception(f"Cannot divide by zero")
        return KinematicVector(self.x / other, self.y / other, self.z / other)

    def __matmul__(self, other) -> float:
        """method calculating scalar product of two vectors
        :param other: second vector
        :return: scalar product of vectors"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def copy(self) -> 'KinematicVector':
        """method returning a copy of the vector
        :return: new vector identical to the original vector"""
        return KinematicVector(self.x, self.y, self.z)


def vector_projection(u, v) -> (KinematicVector, KinematicVector):
    """function calculating the projection of a vector u on the vector v
    :return: parallel and orthogonal (to the vector v) compound of the vector u"""
    alpha = (u @ v) / (v @ v)
    u_star = u * alpha
    return u_star, v - u_star
