import numpy as np
import math
import matplotlib.pyplot as plt

import env

class LidarScanner:
    def __init__(self, pos, range_min=0.1, range_max=100.0,
                            angle_min=-math.pi/2, angle_max = math.pi/2,
                            resolution=math.pi/180, fps=5):
        self.pose = pos # x, y, theta
        self.range_min = range_min
        self.range_max = range_max
        self.angle_min = angle_min
        self.angle_max = angle_max
        self.resolution = resolution
        self.angle_num = int((self.angle_max - self.angle_min)/self.resolution) + 1
        self.range_num = 200
        self.fps = fps
        self.sense_data = []

        self.env = env.Env()
    
    def update_position(self, pos):
        self.pose = pos

    def distance(self, obs_pose):
        ex = obs_pose[0] - self.pose[0]
        ey = obs_pose[1] - self.pose[1]
        return math.hypot(ex, ey)

    def is_colision(self, x, y):
        if self.env.obs_circle is not None:
            for (cx, cy, cr) in self.env.obs_circle:
                ex = cx - x; ey = cy - y
                if ex**2 + ey**2 - cr**2 <= 0:
                    return True
        if self.env.obs_rectangle is not None:
            for (rx, ry, rw, rh) in self.env.obs_rectangle:
                if 0 <= x - rx <= rw and 0 <= y - ry <= rh:
                    return True

        if self.env.obs_boundary is not None:
            for (bx, by, bw, bh) in self.env.obs_boundary:
                if 0 <= x - bx <= bw and 0 <= y - by <= bh:
                    return True

        return False

    def sense_obstacle(self):
        data = []
        x, y, _ = self.pose
        for angle in np.linspace(self.angle_min + self.pose[2], self.angle_max + self.pose[2],
                                self.angle_num, True):
            sense = False
            x1 = x + self.range_min*math.cos(angle)
            y1 = y + self.range_min*math.sin(angle)

            x2 = x + self.range_max*math.cos(angle)
            y2 = y + self.range_max*math.sin(angle)

            for i in range(self.range_num+1):
                u = i/self.range_num
                x3 = x2*u + x1*(1 - u)
                y3 = y2*u + y1*(1 - u)
                if self.is_colision(x3, y3):
                    dis = self.distance((x3, y3))
                    data.append(dis)
                    sense = True
                    break
            if not sense:
                data.append(self.range_max)
        self.sense_data = data

if __name__ == "__main__":
    lidar = LidarScanner((0,0, math.pi/3))
    import time
    st = time.time()
    lidar.sense_obstacle()
    print(time.time() - st)
    print(lidar.sense_data)
    print(len(lidar.sense_data))

# https://www.youtube.com/watch?v=JbUNsYPJK1U