import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/min/a/li5313/ME597Lab1/ros2_ws/install/task_1'
