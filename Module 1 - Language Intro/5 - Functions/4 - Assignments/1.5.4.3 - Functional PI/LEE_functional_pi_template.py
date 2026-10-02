import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###

for i in range(1, 10):
    a = 1.0
    b = 1.0/ (2 ** 0.5)
    t = 0.25
    p = 1.0
    New_A = (a + b) / 2   
    New_B = (a * b) ** 0.5
    New_T = t - p * ((a - New_A) * (a - New_A))
    New_P = p * 2
    #set my og variables = to that new value we got so we acturally iterate as we go through the loop
    a = New_A
    b = New_B
    t = New_T
    p = New_P     
    # change this so an actual value is returned
    return my_pi




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
