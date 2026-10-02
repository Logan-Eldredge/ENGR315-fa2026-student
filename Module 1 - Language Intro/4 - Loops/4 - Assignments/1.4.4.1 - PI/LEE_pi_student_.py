import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
#pi_estimate = 

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
# I defined these values like this because thats what the algorithm calls for
a = 1.0
b = 1.0/ (2 ** 0.5)
t = 0.25
p = 1.0

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###
#start of the loop, define the new values
    New_A = (a + b) / 2
    New_B = (a * b) ** 0.5
    New_T = t - p * ((a - New_A) * (a - New_A))
    New_P = p * 2
    #set my og variables = to that new value we got so we acturally iterate as we go through the loop
    a = New_A
    b = New_B
    t = New_T
    p = New_P     
    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = (a + b) ** 2 / (4 * t)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
