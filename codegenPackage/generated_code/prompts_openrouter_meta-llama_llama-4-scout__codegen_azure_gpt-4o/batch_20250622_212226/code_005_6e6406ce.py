"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: "Develop a disinfection robot, similar to Puductor 2, using ROS and integrating UV-C light disinfection with autonomous navigation."
Generated: DETERMINISTIC_6e6406ce24ea29da
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import time

class DisinfectionRobot:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('disinfection_robot', anonymous=True)

        # Publisher for robot movement
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Publisher for UV-C light control
        self.uv_light_pub = rospy.Publisher('/uv_light', Bool, queue_size=10)

        # Subscriber for laser scan data
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        # Robot state variables
        self.obstacle_detected = False
        self.uv_light_on = False

        # Rate for the main loop
        self.rate = rospy.Rate(10)

    def laser_callback(self, data):
        """
        Callback function for laser scan data.
        Detects obstacles and updates the obstacle_detected flag.
        """
        min_distance = min(data.ranges)
        if min_distance < 0.5:  # Threshold for obstacle detection
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def toggle_uv_light(self, state):
        """
        Toggles the UV-C light on or off.
        :param state: Boolean indicating whether to turn the light on or off.
        """
        self.uv_light_on = state
        uv_msg = Bool()
        uv_msg.data = state
        self.uv_light_pub.publish(uv_msg)

    def move_robot(self, linear_speed, angular_speed):
        """
        Sends movement commands to the robot.
        :param linear_speed: Linear speed in m/s.
        :param angular_speed: Angular speed in rad/s.
        """
        twist = Twist()
        twist.linear.x = linear_speed
        twist.angular.z = angular_speed
        self.cmd_vel_pub.publish(twist)

    def stop_robot(self):
        """
        Stops the robot by sending zero velocity commands.
        """
        self.move_robot(0.0, 0.0)

    def run(self):
        """
        Main loop for the disinfection robot.
        Handles navigation and UV-C light control.
        """
        rospy.loginfo("Disinfection robot started.")
        self.toggle_uv_light(True)  # Turn on UV-C light at startup

        while not rospy.is_shutdown():
            try:
                if self.obstacle_detected:
                    rospy.loginfo("Obstacle detected! Stopping robot.")
                    self.stop_robot()
                    self.toggle_uv_light(False)  # Turn off UV-C light when stopped
                else:
                    rospy.loginfo("No obstacles detected. Moving forward.")
                    self.toggle_uv_light(True)  # Turn on UV-C light while moving
                    self.move_robot(0.2, 0.0)  # Move forward at 0.2 m/s

                self.rate.sleep()
            except rospy.ROSInterruptException:
                rospy.logerr("ROS Interrupt Exception! Stopping robot.")
                self.stop_robot()
                self.toggle_uv_light(False)
                break
            except Exception as e:
                rospy.logerr(f"Unexpected error: {e}")
                self.stop_robot()
                self.toggle_uv_light(False)
                break

        rospy.loginfo("Disinfection robot shutting down.")

if __name__ == '__main__':
    try:
        robot = DisinfectionRobot()
        robot.run()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS node interrupted.")
```

This code is a basic implementation of a disinfection robot using ROS. It integrates UV-C light control and autonomous navigation with obstacle detection.
