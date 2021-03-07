from niryo_one_python_api.niryo_one_api import *
import rospy
import time
import math

rospy.init_node('niryo_one_run_python_api_code')

print "--- Start"

n = NiryoOne()

try:
    n.calibrate_manual()
    n.activate_learning_mode(False)
    n.move_joints([0, 0.6, -0.1322, 0, 0, 0])
    n.move_joints([-0.816, 0, -0.816, 0, -1, 0])
    n.move_joints([-0.816, 0, -0.816, 0, -0.816, 0])
    n.change_tool(TOOL_GRIPPER_2_ID)
    n.get_current_tool_id()
    n.open_gripper(TOOL_GRIPPER_2_ID, 500)
    n.wait(0.2)
    n.close_gripper(TOOL_GRIPPER_2_ID, 500)

    n.change_tool(TOOL_NONE)

    n.activate_learing_mode(True)

except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"
