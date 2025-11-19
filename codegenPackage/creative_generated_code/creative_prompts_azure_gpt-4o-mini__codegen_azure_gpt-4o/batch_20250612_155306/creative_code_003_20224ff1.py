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
"""
Robotics Project: Controlling a Simple Robot
This project simulates a basic robot with movement functionalities.
Elementary students can instruct the robot to move forward, backward, turn left, and turn right.
The program uses logical commands to foster creativity and problem-solving skills.

Requirements:
- Python 3.x
"""

class SimpleRobot:
    """
    A class representing a simple robot with movement capabilities.
    """
    def __init__(self, name="Robo"):
        """
        Initialize the robot with a name and starting position/direction.

        Parameters:
        name (str): The name of the robot.
        """
        self.name = name
        self.position = [0, 0]  # [x, y] coordinates on a 2D grid
        self.direction = "N"   # N (North), E (East), S (South), W (West)
        print(f"{self.name} is initialized at position {self.position} facing {self.direction}.")

    def move_forward(self):
        """
        Move the robot one step forward in the direction it's facing.
        """
        if self.direction == "N":
            self.position[1] += 1
        elif self.direction == "E":
            self.position[0] += 1
        elif self.direction == "S":
            self.position[1] -= 1
        elif self.direction == "W":
            self.position[0] -= 1
        print(f"{self.name} moved forward to position {self.position}.")

    def move_backward(self):
        """
        Move the robot one step backward (opposite to the direction it's facing).
        """
        if self.direction == "N":
            self.position[1] -= 1
        elif self.direction == "E":
            self.position[0] -= 1
        elif self.direction == "S":
            self.position[1] += 1
        elif self.direction == "W":
            self.position[0] += 1
        print(f"{self.name} moved backward to position {self.position}.")

    def turn_left(self):
        """
        Turn the robot 90 degrees to the left.
        """
        directions = ["N", "W", "S", "E"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        print(f"{self.name} turned left and is now facing {self.direction}.")

    def turn_right(self):
        """
        Turn the robot 90 degrees to the right.
        """
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        print(f"{self.name} turned right and is now facing {self.direction}.")

def main():
    """
    Main function to interact with the SimpleRobot class.
    Provides a simple menu for students to control the robot.
    """
    robot = SimpleRobot("RoboJunior")  # Create an instance of the robot

    menu = """
    === Simple Robot Control Menu ===
    Select a command:
    1. Move Forward
    2. Move Backward
    3. Turn Left
    4. Turn Right
    5. Quit
    """

    while True:
        print(menu)
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                robot.move_forward()
            elif choice == 2:
                robot.move_backward()
            elif choice == 3:
                robot.turn_left()
            elif choice == 4:
                robot.turn_right()
            elif choice == 5:
                print("Goodbye! Thank you for controlling RoboJunior.")
                break
            else:
                print("Invalid choice. Please select a valid option (1-5).")
        except ValueError:
            print("Error: Please enter a number between 1 and 5.")

if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
```
