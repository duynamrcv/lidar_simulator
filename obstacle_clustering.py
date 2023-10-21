import math
import numpy as np
from lidar_scanner import LidarScanner

def clustering(lidar:LidarScanner, thresh=10):
    """
    lidar: Lidar information
    thresh: to determine two secutive ray is resulted of same obstacle [cm]
    """
    clusters = []
    cluster = []
    values =[]
    for index,value in enumerate(lidar.sense_data):
        if value == lidar.range_max:
            if cluster != []:
                clusters.append(cluster)
                cluster = []
                values =[]
            continue
        if cluster == []:
            cluster.append(index)
            values.append(value)    
        elif abs(value - values[-1]) < thresh:
            cluster.append(index)
            values.append(value)
        else:
            clusters.append(cluster)
            cluster = [index]
            values = [value]
    if cluster != []:
        clusters.append(cluster)
    return clusters
    