"""
Generated Code Metadata:
========================
Original URL: https://liusanchuan.github.io
Prompt: Generate Python code for remote control of a Turtlebot3 robot and constructing a SLAM map, referencing the steps outlined in the Turtlebot3教程.
Generated: DETERMINISTIC_785600316f46c08d
Batch ID: 20250612_151426
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
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid, Odometry
import tf
from tf.transformations import euler_from_quaternion
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class Turtlebot3Controller:
    def __init__(self):
        rospy.init_node('turtlebot3_controller', anonymous=True)
        
        # Initialize publishers and subscribers
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.map_sub = rospy.Subscriber('/map', OccupancyGrid, self.map_callback)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        # Initialize action client for navigation
        self.move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base_client.wait_for_server()
        
        # Robot state variables
        self.current_pose = None
        self.current_scan = None
        self.current_map = None
        
        # Control parameters
        self.linear_speed = 0.2
        self.angular_speed = 0.5
        self.min_distance = 0.3  # meters
        
        rospy.loginfo("Turtlebot3 controller initialized")

    def scan_callback(self, data):
        """Callback for processing laser scan data."""
        self.current_scan = data

    def map_callback(self, data):
        """Callback for processing map data."""
        self.current_map = data

    def odom_callback(self, data):
        """Callback for processing odometry data."""
        self.current_pose = data.pose.pose

    def get_current_yaw(self):
        """Get current yaw angle from odometry."""
        if self.current_pose is None:
            return None
        orientation_q = self.current_pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        _, _, yaw = euler_from_quaternion(orientation_list)
        return yaw

    def move_forward(self, distance):
        """Move robot forward by specified distance."""
        if self.current_pose is None:
            rospy.logwarn("No odometry data available")
            return False

        start_x = self.current_pose.position.x
        start_y = self.current_pose.position.y
        rate = rospy.Rate(10)
        twist = Twist()
        twist.linear.x = self.linear_speed

        while not rospy.is_shutdown():
            current_x = self.current_pose.position.x
            current_y = self.current_pose.position.y
            traveled = np.sqrt((current_x - start_x)**2 + (current_y - start_y)**2)
            
            if traveled >= distance:
                twist.linear.x = 0
                self.cmd_vel_pub.publish(twist)
                return True
            
            if self.check_obstacle():
                twist.linear.x = 0
                self.cmd_vel_pub.publish(twist)
                rospy.logwarn("Obstacle detected, stopping movement")
                return False
            
            self.cmd_vel_pub.publish(twist)
            rate.sleep()

    def rotate(self, angle):
        """Rotate robot by specified angle (radians)."""
        if self.current_pose is None:
            rospy.logwarn("No odometry data available")
            return False

        start_yaw = self.get_current_yaw()
        target_yaw = start_yaw + angle
        rate = rospy.Rate(10)
        twist = Twist()
        twist.angular.z = self.angular_speed if angle > 0 else -self.angular_speed

        while not rospy.is_shutdown():
            current_yaw = self.get_current_yaw()
            if abs(current_yaw - target_yaw) < 0.1:
                twist.angular.z = 0
                self.cmd_vel_pub.publish(twist)
                return True
            
            self.cmd_vel_pub.publish(twist)
            rate.sleep()

    def check_obstacle(self):
        """Check if obstacle is within minimum distance."""
        if self.current_scan is None:
            return False
        
        ranges = np.array(self.current_scan.ranges)
        ranges = ranges[np.isfinite(ranges)]
        if len(ranges) == 0:
            return False
            
        min_range = np.min(ranges)
        return min_range < self.min_distance

    def navigate_to_goal(self, x, y, theta):
        """Navigate to specified goal using move_base."""
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.z = np.sin(theta / 2)
        goal.target_pose.pose.orientation.w = np.cos(theta / 2)
        
        self.move_base_client.send_goal(goal)
        rospy.loginfo(f"Navigating to goal: ({x}, {y}, {theta})")
        
        wait = self.move_base_client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            return False
        return self.move_base_client.get_result()

    def explore_and_map(self):
        """Simple exploration behavior to build SLAM map."""
        rospy.loginfo("Starting exploration and mapping")
        
        while not rospy.is_shutdown():
            if self.check_obstacle():
                self.rotate(np.pi/2)  # Turn 90 degrees if obstacle detected
            else:
                self.move_forward(0.5)  # Move forward 0.5 meters
            
            if rospy.is_shutdown():
                break

    def stop(self):
        """Stop all robot movement."""
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        self.cmd_vel_pub.publish(twist)

if __name__ == '__main__':
    try:
        controller = Turtlebot3Controller()
        
        # Example usage:
        # controller.move_forward(1.0)  # Move forward 1 meter
        # controller.rotate(np.pi/2)    # Rotate 90 degrees
        # controller.navigate_to_goal(2.0, 3.0, 0.0)  # Navigate to x=2, y=3
        
        # For SLAM mapping:
        # controller.explore_and_map()
        
        rospy.spin()
        
    except rospy.ROSInterruptException:
        controller.stop()
        rospy.loginfo("Turtlebot3 controller shutdown")
```
