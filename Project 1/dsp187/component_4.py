import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import utils

from typing import List, Tuple
from numpy import pi

def interpolate_rigid_body(start_pose: np.ndarray, goal_pose: np.ndarray) -> List[np.ndarray]:
    frames = 30
    start_pose = utils.normalize_angle(start_pose)
    goal_pose = utils.normalize_angle(goal_pose)
    path = [start_pose]
    delta_pose = utils.normalize_angle(goal_pose-start_pose) 
    delta_per_frame = delta_pose/frames
    for f in range(frames):
        next_pose = path[f] + delta_per_frame
        path.append(next_pose)
    return path
def forward_propagate_rigid_body(start_pose: np.ndarray, Plan: List[Tuple[np.ndarray, float]]) -> List[np.ndarray]:
    path = [start_pose]
    prev_pose = path[0]
    for v_dot, dur in Plan:
        v_dot = utils.normalize_angle(v_dot)
        next_pose = prev_pose + (v_dot)*dur
        path.append(next_pose)
        prev_pose = next_pose
    return path
    pass

def draw_2arm_and_frame(ax, pose: np.ndarray, l1=2, l2=1.5, w=.3, ec='r'):
    thetas_deg = np.rad2deg(pose)
    
    ax.quiver(0, 0, 1, 0, width=.003, color='b') 
    ax.add_patch(patches.Rectangle((0, -w/2), l1, w, angle=thetas_deg[0, 0], rotation_point=(0, 0), ec=ec, fc='none'))
    ax.quiver(0, 0, np.cos(pose[0, 0]), np.sin(pose[0, 0]), width=.003, color=ec)
    
    R1 = utils.angle_to_rotation_matrix(pose[0, 0]) 
    t1 = utils.xy_to_t(l1, 0)
    l1_x_end, l1_y_end = utils.t_to_xy(R1@t1)
    ax.quiver(l1_x_end, l1_y_end, np.cos(pose[0, 0]), np.sin(pose[0, 0]), width=.003, color='b')
    ax.add_patch(patches.Rectangle((l1_x_end-w/2, l1_y_end-w/2), l2, w, angle=thetas_deg[0, 0]+thetas_deg[1, 0], rotation_point=(l1_x_end, l1_y_end), ec=ec, fc='none'))
    ax.quiver(l1_x_end, l1_y_end, np.cos(pose[0, 0] + pose[1, 0]), np.sin(pose[0, 0] + pose[1, 0]), width=.003, color=ec)

    R2 = utils.angle_to_rotation_matrix(pose[1, 0])
    t2 = utils.xy_to_t(l2-w/2, 0)
    end_x, end_y = utils.t_to_xy(R1@R2@t2 + R1@t1)
    ax.plot(end_x, end_y, 'go')

def visualize_path(path: List[np.ndarray]):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1, xlim=(-10,10), ylim=(-10, 10), aspect='equal')

    # Animation Code START
    def draw(pose):
        ax.cla()
        ax.set_xlim((-10,10))
        ax.set_ylim((-10,10))
        plt.grid()
        draw_2arm_and_frame(ax, pose)
    anim =  animation.FuncAnimation(fig=fig, func=draw, frames=path, interval=1000/len(path))
    # Set to false if you do not want to export the gif
    export = True
    if export:
        anim.save("component_4ii.gif")
    # Animation Code END

    # View all frames START
    # plt.grid()
    # for pose in path:
    #     draw_2arm_and_frame(ax, pose)
    # View all frames END

    
    plt.show()
def test():
    start_pose = np.array([[0, pi/8]]).T
    goal_pose = np.array([[-9*pi/8, -3*pi/4]]).T

    Plan = [
        (np.array([[9*pi/2, -pi/16]]).T, 2),
        (np.array([[pi/4, pi/4]]).T, 1),
        (np.array([[-pi/4, pi/2]]).T, 3)
    ]

    # visualize_path(interpolate_rigid_body(start_pose, goal_pose))
    visualize_path(forward_propagate_rigid_body(start_pose, Plan))
    pass

if __name__ == "__main__":
    test()