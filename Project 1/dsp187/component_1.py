# Question 1
import matplotlib
import numpy as np

def inErrorTolerance(i: float, j: float, e) -> bool:
    if abs(i-j) > e:
        return False
    return True

def check_SOn(m: np.ndarray, epsilon=0.01) -> bool:
    if not (m.shape == (2,2) or m.shape == (3,3)):
        return False
    
    x = m.T @ m
    I = np.eye(m.shape[0])
    for r, c in np.ndindex(m.shape):
        x_rc = x[r,c]
        I_rc = I[r,c]
        if(not inErrorTolerance(x_rc, I_rc, epsilon)): #TODO: check edge cases
            return False

    if not inErrorTolerance(np.linalg.det(m), 1, epsilon):
        return False
    return True
def check_quaternion(v: np.array, epsilon=0.01) -> bool:
    if not v.shape == (4,1):
        return False
    if not inErrorTolerance(np.sum(v**2), 1, epsilon):
        return False
    return True

def check_SEn(m: np.ndarray, epsilon=0.01) -> bool:
    if not (m.shape == (3,3) or m.shape == (4,4)):
        return False
    n = m.shape[0]
    R = m[0:n-1, 0:n-1]
    t = m[0:n-1, n-1] # t can be anything.
    bottomRow = m[n-1]
    ideal_bottomRow = np.eye(1, n, n-1)[0]
    if not check_SOn(R, epsilon):
        return False
    for i, j in zip(bottomRow, ideal_bottomRow):
        if not inErrorTolerance(i, j, epsilon):
            return False
    return True


def test():
    pose_2d = np.array([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
    pose_3d = np.array([[0.0163444,  0.2784235,  0.9603193, -5],
                        [0.6589425,  0.7193688, -0.2197802, 21321],
                        [-0.7520158,  0.6363873, -0.1717075, .25 ],
                        [-0.0000001,  0, 0, 1.0000001 ]])
    assert check_SEn(pose_2d)
    assert check_SEn(pose_3d)

if __name__ == "__main__":
    test()