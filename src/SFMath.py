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
                if type(value) not in TYPES_TO_FLOAT:
                    raise Exception(f"Argument '{str(key)}' must be one of this types: {str(TYPES_TO_FLOAT)} not {str(type(value))}")
                print(key)
                match key:
                    case "x":
                        self.x = float(value)
                    case "y":
                        self.y = float(value)
                    case "z":
                        self.z = float(value)
                    case _:
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

    def __add__(self, other: 'KinematicVector') -> 'KinematicVector':
        """method summing two vectors
        :param other: second vector to add
        :return: sum of the vectors"""
        if type(other) != KinematicVector:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        return KinematicVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'KinematicVector') -> 'KinematicVector':
        """method subtracting two vectors
        :param other: second vector to subtract
        :return: difference of the vectors"""
        if type(other) != KinematicVector:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        return KinematicVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float | int) -> 'KinematicVector':
        """method multiplying scalar and a vector
        :param other: number to multiply
        :return: vectors multiplied by the scalar"""
        if type(other) not in TYPES_TO_FLOAT:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        return KinematicVector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float | int) -> 'KinematicVector':
        """method dividing vector by a scalar
        :param other: number to divide
        :return: vectors multiplied by the scalar"""
        if type(other) not in TYPES_TO_FLOAT:
            raise Exception(f"The {other} argument has an incorrect type {type(other)}")
        if other == 0:
            raise Exception(f"Cannot divide by zero")
        return KinematicVector(self.x / other, self.y / other, self.z / other)

    def __matmul__(self, other: 'KinematicVector') -> float:
        """method calculating scalar product of two vectors
        :param other: second vector
        :return: scalar product of vectors"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def copy(self) -> 'KinematicVector':
        """method returning a copy of the vector
        :return: new vector identical to the original vector"""
        return KinematicVector(self.x, self.y, self.z)

    def __eq__(self, other: 'KinematicVector') -> bool:
        """method checking if two vectors are equal
        :return: result of the comparison"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: 'KinematicVector') -> bool:
        """method checking if two vectors are not equal
        :return: result of the comparison"""
        return not self == other

    def __nonzero__(self) -> bool:
        return abs(self) > 0.0

class CoordinateSystem:
    def __init__(self, *args, **kwargs) -> None:
        """class' constructor
        :param *args: arbitrary positional arguments:
        - 0 parameters - () - create a default coordinate system:
            vx = (1,0,0), vy = (0,1,0), vz = (0,0,1)
        - 1 parameter - (a) - create a scaled default coordinate system:
            vx = (a,0,0), vy = (0,a,0), vz = (0,0,a)
        - 3 parameters - (a,b,c) - create a custom coordinate system:
            vx = a, vy = b, vz = c
        :param **kwargs: arbitrary keyword arguments:
        - vx = a - vector vx = a,
        - vy = b - vector vx = b,
        - vz = c - vector vx = c,
        :return: None"""
        self.vx = KinematicVector(1, 0, 0)
        self.vy = KinematicVector(0, 1, 0)
        self.vz = KinematicVector(0, 0, 1)
        if args:
            match len(args):
                case 1:
                    if type(args[0]) not in TYPES_TO_FLOAT:
                        raise Exception(f"Argument '{str(args[0])}' must be one of this types: {str(TYPES_TO_FLOAT)}")
                    self.vx = KinematicVector(1, 0, 0) * args[0]
                    self.vy = KinematicVector(0, 1, 0) * args[0]
                    self.vz = KinematicVector(0, 0, 1) * args[0]
                case 3:
                    if type(args[0]) != KinematicVector:
                        raise Exception(f"Argument '{str(args[0])}' must be type: {KinematicVector}")
                    if type(args[1]) != KinematicVector:
                        raise Exception(f"Argument '{str(args[1])}' must be type: {KinematicVector}")
                    if type(args[2]) != KinematicVector:
                        raise Exception(f"Argument '{str(args[2])}' must be type: {KinematicVector}")
                    self.vx = args[0].copy()
                    self.vy = args[1].copy()
                    self.vz = args[2].copy()
                case _:
                    raise Exception(f"You can use 0, 1 or 3 arbitrary arguments, but there is {str(len(args))}")
        if kwargs:
            for key, value in kwargs.items():
                if type(value) != KinematicVector:
                    raise Exception(f"Argument '{str(value)}' must be type: {KinematicVector} not {str(type(value))}")
                match key:
                    case "vx":
                        self.vx = value.copy()
                    case "vy":
                        self.vy = value.copy()
                    case "vz":
                        self.vz = value.copy()
                raise Exception(f"Incorrect keyword argument: {str(key)}")

    def __repr__(self):
        """method returning a string representation of the coordinate system
        :return: a string representation of the coordinate system"""
        return f"[{self.vx},\n {self.vy},\n {self.vz}]"



def vector_projection_1d(u: KinematicVector, v: KinematicVector) -> (KinematicVector, KinematicVector):
    """function calculating the projection of a vector u on the vector v
    :return: parallel and orthogonal (to the vector v) compound of the vector u"""
    alpha = (u @ v) / (v @ v)
    u_star = u * alpha
    return u_star, v - u_star
