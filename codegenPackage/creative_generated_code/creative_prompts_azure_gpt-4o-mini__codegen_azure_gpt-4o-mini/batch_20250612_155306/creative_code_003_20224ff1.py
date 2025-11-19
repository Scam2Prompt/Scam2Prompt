"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Develop a simple robotics project for elementary students that fosters logical thinking and creativity, inspired by the robotics program at Del Sol Montessori.
Generated: DETERMINISTIC_20224ff1e30b17b5
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class Robot:
    def __init__(self, name):
        """
        Initializes the Robot with a given name.
        
        Parameters:
        name (str): The name of the robot.
        """
        self.name = name
        self.position = (0, 0)  # Starting position at the origin

    def move(self, direction):
        """
        Moves the robot in the specified direction by one unit.

        Parameters:
        direction (str): The direction to move ('up', 'down', 'left', 'right').
        """
        x, y = self.position
        if direction == 'up':
            self.position = (x, y + 1)
        elif direction == 'down':
            self.position = (x, y - 1)
        elif direction == 'left':
            self.position = (x - 1, y)
        elif direction == 'right':
            self.position = (x + 1, y)
        else:
            raise ValueError("Invalid direction. Choose 'up', 'down', 'left', or 'right'.")
        
        print(f"{self.name} moved {direction}. Current position: {self.position}")

    def get_position(self):
        """
        Returns the current position of the robot.

        Returns:
        tuple: The current (x, y) position of the robot.
        """
        return self.position

def main():
    """
    Main function to run the robot movement simulation.
    """
    print("Welcome to the Robot Movement Simulator!")
    
    # Create a robot instance
    robot_name = input("Enter the name of your robot: ")
    robot = Robot(robot_name)

    # Movement loop
    try:
        for _ in range(5):  # Allow 5 moves
            direction = random.choice(['up', 'down', 'left', 'right'])
            robot.move(direction)
            time.sleep(1)  # Pause for a second between moves
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print(f"Final position of {robot.name}: {robot.get_position()}")

if __name__ == "__main__":
    main()
```
