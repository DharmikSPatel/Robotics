import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import utils
import numpy as np
from typing import List, Tuple
from numpy import pi

def interpolate_rigid_body(start_pose: np.ndarray, goal_pose: np.ndarray) -> List[np.ndarray]:
    frames = 30
    
    start_pose[2, 0] = utils.normalize_angle(start_pose[2, 0])
    goal_pose[2, 0] = utils.normalize_angle(goal_pose[2, 0])
    # print(start_pose)
    # print(goal_pose)
    path = [start_pose]
    delta_pose = (goal_pose-start_pose)
    delta_pose[2, 0] = utils.normalize_angle(delta_pose[2, 0])
    # print(delta_pose)
    delta_per_frame = delta_pose/frames
    for f in range(frames):
        next_pose = path[f] + delta_per_frame
        path.append(next_pose)

    # given a 
    #   start pose
    #   end pose
    # return   
    #   List of poses
    # how small distance?

    return path
    pass
def forward_propagate_rigid_body(start_pose: np.ndarray, Plan: List[Tuple[np.ndarray, float]]) -> List[np.ndarray]:
    path = [start_pose]
    prev_pose = path[0]
    for v_dot, dur in Plan:
        v_dot[2, 0] = utils.normalize_angle(v_dot[2, 0])
        next_pose = prev_pose + v_dot*dur
        path.append(next_pose)
        prev_pose = next_pose
    return path
    # given a 
    #   start pose
    #   Plan: List of (velocity, duration) of len N
    # return   
    #   List of poses of len N+1
    # how small distance?
    pass
def draw_rectangle_and_frame(ax, pose: np.ndarray, w=.5, h=.2, ec='r'):
    theta_deg = np.rad2deg(pose[2])
    ax.add_patch(patches.Rectangle((pose[0, 0]-w/2, pose[1, 0]-h/2), w, h, angle=theta_deg, rotation_point=(pose[0, 0], pose[1, 0]), ec=ec, fc='none'))

    ax.quiver(pose[0], pose[1], np.cos(pose[2]), np.sin(pose[2]), width=.003, color=ec)
def visualize_path(path: List[np.ndarray]):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1, xlim=(-10,10), ylim=(-10, 10), aspect='equal')
    
    # Animation Code START
    def draw(pose):
        ax.cla()
        ax.set_xlim((-10,10))
        ax.set_ylim((-10,10))
        plt.grid()
        draw_rectangle_and_frame(ax, pose)
    anim =  animation.FuncAnimation(fig=fig, func=draw, frames=path, interval=1000/len(path))
    # Set to false if you do not want to export the gif
    export = False
    if export:
        anim.save("component_3ii.gif")
    # Animation Code END

    # View all frames START
    # plt.grid()
    # for pose in path:
    #     draw_rectangle_and_frame(ax, pose)
    # View all frames END
    
    
    plt.show()

def test():
    start_pose=np.array([[-5, 2.5, pi/2]]).T
    goal_pose=np.array([[5, -5, -7*pi/8]]).T

    Plan = [
        (np.array([[1, 1, pi/4]]).T, 4),
        (np.array([[0, -1, pi/8]]).T, 2),
        (np.array([[1, -1, pi/8]]).T, 10)
    ]
    visualize_path(interpolate_rigid_body(start_pose, goal_pose))
    # visualize_path(forward_propagate_rigid_body(start_pose, Plan))
    pass

if __name__ == "__main__":
    test()
