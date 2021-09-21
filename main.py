import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from env import Env
from lidar_scanner import LidarScanner

def plot_robot(lidar):
    # Plot environment
    fig, ax = plt.subplots()
    if lidar.env.obs_boundary is not None:
        for (ox, oy, w, h) in lidar.env.obs_boundary:
            ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    edgecolor='black',
                    facecolor='black',
                    fill=True
                )
            )

    if lidar.env.obs_rectangle is not None:
        for (ox, oy, w, h) in lidar.env.obs_rectangle:
            ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    edgecolor='black',
                    facecolor='gray',
                    fill=True
                )
            )

    if lidar.env.obs_circle is not None:
        for (ox, oy, r) in lidar.env.obs_circle:
            ax.add_patch(
                patches.Circle(
                    (ox, oy), r,
                    edgecolor='black',
                    facecolor='gray',
                    fill=True
                )
            )

    plt.plot(x, y, "rs", linewidth=20)

    for i in range(len(lidar.sense_data)):
        angle = lidar.angle_min + lidar.pose[2] + lidar.resolution*i
        rayx = [lidar.pose[0], lidar.pose[0]+math.cos(angle)*lidar.sense_data[i]]
        rayy = [lidar.pose[1], lidar.pose[1]+math.sin(angle)*lidar.sense_data[i]]
        plt.plot(rayx, rayy, '-b', linewidth=0.5)

    plt.title("Lidar Scanner")
    plt.axis("equal")
    plt.pause(2)

if __name__ == "__main__":
    # lidar
    xs = [50, 200, 500, 400]
    ys = [200, 20, 400, 500]
    thetas = [math.pi/2, math.pi/3, math.pi, -5*math.pi/6]
    for i in range(4):
        x = xs[i]; y = ys[i]; theta = thetas[i]
        lidar = LidarScanner((x, y, theta))
        lidar.sense_obstacle()
        plot_robot(lidar)
    
    plt.show()