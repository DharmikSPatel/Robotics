# Question 1
import matplotlib
import numpy

# How to check error? .1   Real: 1, get: .95 then it works right?

def check_SOn(matrix: m, float: epsilon=0.01) -> bool:
    # 2d or 3d

    # Check:
    # square matrix(2d or 3d)
    # R_trans*R = I within error
    # detR = 1 within error
    pass
def check_quaternion(vector: v, float: epsilon=0.01) -> bool:
    # check that x^2+y^2+z^2+w^z = 1
    pass
def check_SEn(matrix: m, float: epsilon=0.01) -> bool:
    # matrix with rotation and transformation aka a pose
    #2d or 3d

    #check that top right of matrix is rotation
    #check bottom is 0s and 1s
    #check last column is any random numbers and 1
    pass
