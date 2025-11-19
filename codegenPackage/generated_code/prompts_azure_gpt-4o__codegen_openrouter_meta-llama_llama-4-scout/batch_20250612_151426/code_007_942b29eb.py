"""
Generated Code Metadata:
========================
Original URL: https://liusanchuan.github.io
Prompt: Provide a Python example for integrating Turtlebot3 with OpenCR and Raspberry Pi 3, referencing the configuration process described in the Turtlebot3教程.
Generated: DETERMINISTIC_942b29eb4b612cd9
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import rospy
import serial
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

# Define constants
PORT = '/dev/ttyUSB0'  # OpenCR port
BAUDRATE = 115200  # Baudrate for serial communication
RASPBERRY_PI_IP = '192.168.1.100'  # IP address of Raspberry Pi 3

class Turtlebot3OpenCR:
    def __init__(self):
        self.serial_connection = serial.Serial(PORT, BAUDRATE, timeout=1)
        self.joint_state_pub = rospy.Publisher('joint_states', JointState, queue_size=10)
        self.cmd_vel_sub = rospy.Subscriber('cmd_vel', Twist, self.cmd_vel_callback)

    def cmd_vel_callback(self, msg):
        # Convert Twist message to OpenCR commands
        linear_velocity = msg.linear.x
        angular_velocity = msg.angular.z

        # Send commands to OpenCR
        self.serial_connection.write(f'motor 1 {linear_velocity}\n'.encode())
        self.serial_connection.write(f'motor 2 {angular_velocity}\n'.encode())

    def get_joint_states(self):
        # Read joint states from OpenCR
        self.serial_connection.write('joint_states\n'.encode())
        response = self.serial_connection.readline().decode().strip()
        joint_states = response.split(',')

        # Create and publish JointState message
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = ['wheel_left', 'wheel_right']
        joint_state_msg.position = [float(joint_states[0]), float(joint_states[1])]
        self.joint_state_pub.publish(joint_state_msg)

def main():
    try:
        rospy.init_node('turtlebot3_opencr')
        turtlebot3_opencr = Turtlebot3OpenCR()

        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            turtlebot3_opencr.get_joint_states()
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    except serial.SerialException as e:
        rospy.logerr(f'Serial exception: {e}')
    finally:
        rospy.shutdown()

if __name__ == '__main__':
    main()
```
