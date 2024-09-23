import numpy as np
from numpy import sin, cos, pi, arctan2
def normalize_angle(angle: float | np.ndarray):
    return (angle + pi) % (2*pi) - pi
def angle_to_rotation_matrix(theta: float) -> np.ndarray:
    return np.array([[cos(theta), -sin(theta)], 
                       [sin(theta),  cos(theta)]])
def rotation_matrix_to_anlge(R: np.ndarray) -> float:
    return arctan2(R[1, 0], R[0,0])
def xy_to_t(x, y) -> np.ndarray:
    # col vector
    return np.array([[x, y]]).T
def t_to_xy(t: np.ndarray) -> np.ndarray:
    # row vector, which will be unpacked to x,y
    return t.T[0]
def euler_to_transformation_matrix(p: np.ndarray) -> np.ndarray:
    R = angle_to_rotation_matrix(p[2])
    t = xy_to_t(p[0], p[1])
    top = np.concatenate((R, t), axis=1)
    bot = np.eye(1, 3, 3-1)
    return np.concatenate((top, bot), axis=0)

def test_1():
    for i in range(1000):
        theta = (np.random.rand() * 10) - 5
        R = angle_to_rotation_matrix(theta)
        p_theta = rotation_matrix_to_anlge(R)
        # print(normalize_angle(theta))
        # print(R)
        # print(p_theta)
        # print(abs(normalize_angle(theta) - p_theta))
        assert abs(normalize_angle(theta) - p_theta) <= .0001
def test_2():
    p = (np.random.rand(3) * 10) - 5
    R = angle_to_rotation_matrix(p[2])
    # print(p)
    # print(R)
    T = euler_to_transformation_matrix(p)
    # print(T)

if __name__ == "__main__":
    test_2()