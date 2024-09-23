# Question 2
import matplotlib.pyplot as plt
import numpy as np
from typing import List
from component_1 import check_SOn, check_quaternion
def random_euler_angle(min=0, max=2*np.pi):
    return np.random.rand()*2*np.pi
def rotation_matrix_across_x(angle: float) -> np.ndarray:
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([[1, 0, 0],
                    [0, cos, -sin],
                    [0, sin, cos]])
def rotation_matrix_across_y(angle: float) -> np.ndarray:
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([[cos, 0, sin],
                    [0, 1, 0],
                    [-sin, 0, cos]])
def rotation_matrix_across_z(angle: float) -> np.ndarray:
    sin = np.sin(angle)
    cos = np.cos(angle)
    R = np.array([[cos, -sin, 0],
                    [sin, cos, 0],
                    [0, 0, 1]])
    return R
def algo_rotation_matrix_across_z(angle: float) -> np.ndarray:
    sin = np.sin(angle)
    cos = np.cos(angle)
    R = np.array([[cos, sin, 0],
                    [-sin, cos, 0],
                    [0, 0, 1]])
    return R
def rotation_matrix_3d(a1, a2, a3: float) -> np.ndarray:
    return rotation_matrix_across_x(a1) @ rotation_matrix_across_y(a2) @ rotation_matrix_across_z(a3)
def random_rotation_matrix(naive: bool) -> np.array:
    if naive:
        a1 = random_euler_angle()
        a2 = random_euler_angle()
        a3 = random_euler_angle()
        R = rotation_matrix_3d(a1, a2, a3)
        return R
    else:
        theta = random_euler_angle()
        phi = random_euler_angle()
        z = np.random.rand()
        V = np.array([np.cos(phi) * np.sqrt(z),
                      np.sin(phi) * np.sqrt(z),
                      np.sqrt(1-z)]) [np.newaxis]
        R = (2 * np.outer(V, V) - np.eye(3)) @ algo_rotation_matrix_across_z(theta)
        return R
def random_quaternion(naive: bool) -> np.array:
    if naive:
        v = np.random.rand(4,1)
        norm = np.linalg.norm(v)
        Q = v if norm == 0 else v / norm
        return Q
    else:
        s = np.random.rand()
        sigma1 = np.sqrt(1-s)
        sigma2 = np.sqrt(s)
        theta1 = 2*np.pi*np.random.rand()
        theta2 = 2*np.pi*np.random.rand()
        w = np.cos(theta2) * sigma2
        x = np.sin(theta1) * sigma1
        y = np.cos(theta1) * sigma1
        z = np.sin(theta2) * sigma2
        Q = np.array([[w, x, y, z]]).T
        return Q 
def display_rotations(ax, R: np.ndarray):
    # used in reports
    e = 1
    v0 = np.array([[0, 0, 1]]).T
    v1 = np.array([[0, e, 0]]).T + v0
    v0Prime = R@v0
    v1Prime = R@v1 - v0
    x, y, z = v0Prime
    u, w, v = v1Prime
    ax.quiver(x, y, z, u, v, w, length=0.2, arrow_length_ratio =.6, normalize=True)
def test():
    for i in range(1000):
        assert check_SOn(random_rotation_matrix(naive=False))
    for i in range(1000):
        assert check_SOn(random_rotation_matrix(naive=True))
    for i in range(1000):
        assert check_quaternion(random_quaternion(naive=False))
    for i in range(1000):
        assert check_quaternion(random_quaternion(naive=True))       
def test_display():
    # used in reports
    fig, axes = plt.subplots(1, 2, figsize=(12, 8), subplot_kw={"projection": "3d"})
    s = -1
    T = ["Naive Method for Random Rotation Matrix Generation", "Uniform Method for Random Rotation Matrix Generation"]
    B = [True, False]

    for ax, b, title in zip(axes, B, T):
        ax.set_zlim3d(-s, s)
        ax.set_ylim3d(-s, s)
        ax.set_xlim3d(-s, s)
        ax.view_init(elev=0, azim=-90, roll=90)
        ax.set_aspect('equal')
        ax.set_title(title)
        for _ in range(1000):
            R = random_rotation_matrix(naive=b)
            display_rotations(ax, R)
    plt.show()
if __name__ == "__main__":
    test()
    test_display()

