import math
from matplotlib import pyplot as plt
import numpy as np


class Complex:
    def __init__(self, parameter1, parameter2, exp=True):
        if exp:
            self.r = parameter1
            self.theta = parameter2
            self.a = self.r * math.sin(self.theta)
            self.b = self.r * math.cos(self.theta)
        else:
            self.a = parameter1
            self.b = parameter2
            self.r = (parameter1 ** 2 + parameter2 ** 2) ** 0.5
            self.theta = math.atan(
                parameter2/parameter1) if parameter1 != 0 else 0

    def mag(self):
        return self.r

    def __mul__(self, other):
        # ADD CODE FOR HOW TO HANDLE MULTIPLICATION WITH REAL NUMBERS
        if type(other) == Complex:
            return Complex(self.r * other.r, self.theta + other.theta)
        else:
            return Complex(self.r * other, self.theta)

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b, exp=False)

    __rmul__ = __mul__


def discrete_fourier_transform(x_list, fx_list, omega_step, max_omega):

    omega_list, fomega_list_mag = [], []
    for omega in omega_step * np.array(range(-int(max_omega/omega_step), int(max_omega/omega_step))):
        integral_val = Complex(0, 0)
        for x_val, fx_val in zip(x_list, fx_list):
            integral_val += (fx_val * Complex(1, -omega * x_val))

        omega_list.append(omega)
        fomega_list_mag.append((integral_val * (0.5/math.pi)).r)

    return omega_list, fomega_list_mag


# Generating input data for Fourier Transform
x = 0.1 * np.array(range(-100, 100))
fx = np.sin(5 * x) + np.sin(1 * x) + np.sin(7 * x)

plt.plot(x, fx, color="blue")
plt.show()

omega_step, omega_max = 0.01, 10

omega_list, fwmag_list = discrete_fourier_transform(
    x, fx, omega_step, omega_max)

plt.plot(omega_list, fwmag_list, 8)

plt.show()
