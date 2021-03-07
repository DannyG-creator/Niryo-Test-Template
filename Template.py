#Template for Niryo One

from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math

rospy.init_node("Template")

print "--- Start"

n = NiryoOne()

try:
    #auto calibration if Niryo is not centered and aligned
    # n.calibrate_auto()

    #manual if you've already aligned the Niryo (Recommended)
    n.calibrate_manual()
    #turn off learning mode
    n.activate_learning_mode(False)

    #START OF INSTRUCTIONS/CODE




    #END OF INSTRUCTIONS/CODE

    #turn on learning mode
    n.activate_learing_mode(True)

except NiryoOneException as e:
    print e
    #handle exceptions here

print "--- End"
