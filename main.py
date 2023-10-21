import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from env import Env
from lidar_scanner import LidarScanner
from obstacle_clustering import clustering

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

    plt.plot(lidar.pose[0], lidar.pose[1], "rs", linewidth=20)

    for i in range(len(lidar.sense_data)):
        angle = lidar.angle_min + lidar.pose[2] + lidar.resolution*i
        rayx = [lidar.pose[0], lidar.pose[0]+math.cos(angle)*lidar.sense_data[i]]
        rayy = [lidar.pose[1], lidar.pose[1]+math.sin(angle)*lidar.sense_data[i]]
        plt.plot(rayx, rayy, '-b', linewidth=0.5)

    plt.title("Lidar Scanner")
    plt.axis("equal")
    plt.pause(2)

def main1():
    lidar = LidarScanner((0, 0, 0))
    # lidar
    xs = [50, 200, 500, 350]
    ys = [200, 20, 400, 450]
    thetas = [math.pi/2, math.pi/3, math.pi, -5*math.pi/6]
    for i in range(4):
        pos =  (xs[i], ys[i], thetas[i])
        lidar.update_position(pos)
        print(lidar.pose)
        lidar.sense_obstacle()
        plot_robot(lidar)
    
    plt.show()

def main2():
    pos = (350, 450, -5*math.pi/6)
    lidar = LidarScanner(pos)
    lidar.sense_obstacle()

    # print("Sensed data: ", lidar.sense_data)
    plot_robot(lidar)
    plt.figure()
    angles = np.arange(lidar.angle_min, lidar.angle_max+lidar.resolution, lidar.resolution)
    plt.scatter(angles, lidar.sense_data)  
    clusters = clustering(lidar)
    for cluster in clusters:
        plt.scatter(angles[cluster[0]:cluster[-1]+1], lidar.sense_data[cluster[0]:cluster[-1]+1])
    
    plt.show()

if __name__ == "__main__":
    # main1()
    main2()