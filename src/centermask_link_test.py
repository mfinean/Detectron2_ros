#!/usr/bin/env python
import sys
import threading
import time

import cv2 as cv
import numpy as np
import rospy
# from detectron2.config import get_cfg
# from detectron2.data import MetadataCatalog
from cv_bridge import CvBridge, CvBridgeError
# import some common detectron2 utilities
# from detectron2.engine import DefaultPredictor
# from detectron2.utils.logger import setup_logger
# from detectron2.utils.visualizer import Visualizer
# from detectron2_ros.msg import Result
# from centermask.modelling import *
from centermask import *
from sensor_msgs.msg import Image, RegionOfInterest


def main(argv):
    rospy.init_node('detectron2_ros')

if __name__ == '__main__':
    main(sys.argv)
