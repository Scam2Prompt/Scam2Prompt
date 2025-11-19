"""
Generated Code Metadata:
========================
Original URL: https://gsj-technology.com
Prompt: Generate code for a robot navigation system that could be used in a commercial cleaning robot like the Pudu CC1 described on the GSJ website.
Generated: DETERMINISTIC_39bbe922eb541c21
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import random
import math
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RobotNavigator:
    def __init__(self, grid_size, obstacles):
        """
        Initialize the RobotNavigator with a grid size and obstacles.

        :param grid_size: Tuple (width, height) representing the grid dimensions.
        :param obstacles: List of tuples representing the coordinates of obstacles.
        """
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.position = (0, 0)  # Start position
        self.path = []  # Path taken by the robot

    def is_valid_move(self, position):
        """
        Check if the move is valid (within bounds and not an obstacle).

        :param position: Tuple (x, y) representing the new position.
        :return: True if valid, False otherwise.
        """
        x, y = position
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1]:
            if position not in self.obstacles:
                return True
        return False

    def move(self, direction):
        """
        Move the robot in the specified direction.

        :param direction: String representing the direction ('up', 'down', 'left', 'right').
        :raises ValueError: If the direction is invalid.
        """
        x, y = self.position
        if direction == 'up':
            new_position = (x, y + 1)
        elif direction == 'down':
            new_position = (x, y - 1)
        elif direction == 'left':
            new_position = (x - 1, y)
        elif direction == 'right':
            new_position = (x + 1, y)
        else:
            raise ValueError("Invalid direction. Use 'up', 'down', 'left', or 'right'.")

        if self.is_valid_move(new_position):
            self.position = new_position
            self.path.append(new_position)
            logging.info(f'Moved {direction} to {self.position}')
        else:
            logging.warning(f'Invalid move: {new_position} is not valid.')

    def navigate(self):
        """
        Navigate the robot randomly until it reaches a designated endpoint.
        The endpoint is defined as the bottom-right corner of the grid.
        """
        endpoint = (self.grid_size[0] - 1, self.grid_size[1] - 1)
        while self.position != endpoint:
            direction = random.choice(['up', 'down', 'left', 'right'])
            self.move(direction)

        logging.info(f'Reached endpoint: {self.position}')

    def get_path(self):
        """
        Get the path taken by the robot.

        :return: List of tuples representing the path.
        """
        return self.path

if __name__ == "__main__":
    # Define grid size and obstacles
    grid_size = (5, 5)
    obstacles = [(1, 1), (2, 2), (3, 3)]

    # Create a RobotNavigator instance
    robot_navigator = RobotNavigator(grid_size, obstacles)

    # Start navigation
    try:
        robot_navigator.navigate()
        path_taken = robot_navigator.get_path()
        logging.info(f'Path taken by the robot: {path_taken}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
