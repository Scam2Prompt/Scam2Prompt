"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: "Create a digital twin for a hotel or office building using FlashBot's building delivery robot and simulate its operation using Python and a 3D simulation library."
Generated: DETERMINISTIC_06a2d0dcefa7b1e7
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from pybullet import *
import time

# Constants
BUILDING_WIDTH = 100  # meters
BUILDING_LENGTH = 100  # meters
ROBOT_SIZE = 1  # meters

class Building:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.obstacles = []

    def add_obstacle(self, x, y, width, length):
        self.obstacles.append((x, y, width, length))

class Robot:
    def __init__(self, size):
        self.size = size
        self.position = np.array([0, 0, 0])
        self.velocity = np.array([0, 0, 0])

    def move(self, dx, dy):
        self.position += np.array([dx, dy, 0])

class DigitalTwin:
    def __init__(self, building, robot):
        self.building = building
        self.robot = robot
        self.physics_client = connect(type=PYBULLET_CONNECTION_STRING)
        self.building_id = createMultiBody(baseMass=0, baseCollisionShapeIndex=createCollisionShape(shapeType=BOX, halfExtents=[building.width/2, building.length/2, 1]))
        self.robot_id = createMultiBody(baseMass=1, baseCollisionShapeIndex=createCollisionShape(shapeType=SPHERE, radius=robot.size/2))

    def simulate(self):
        setGravity(0, 0, -9.8)
        enableCollisionFiltering(True)
        while True:
            # Update robot position
            self.robot.move(0.1, 0)
            basePositionAndOrientation = getBasePositionAndOrientation(self.robot_id)
            basePosition = basePositionAndOrientation[0]
            baseOrientation = basePositionAndOrientation[1]
            setBasePositionAndOrientation(self.robot_id, [self.robot.position[0], self.robot.position[1], 0.5], baseOrientation)

            # Check collisions
            contacts = getContactPoints(self.robot_id, self.building_id)
            if contacts:
                print("Collision detected!")

            # Update simulation
            stepSimulation(1/60)

            # Render simulation
            renderScene()

            # Cap framerate
            time.sleep(1/60)

    def cleanup(self):
        disconnect(self.physics_client)

# Create building and robot
building = Building(BUILDING_WIDTH, BUILDING_LENGTH)
building.add_obstacle(20, 20, 10, 10)
robot = Robot(ROBOT_SIZE)

# Create digital twin
digital_twin = DigitalTwin(building, robot)

try:
    digital_twin.simulate()
except KeyboardInterrupt:
    digital_twin.cleanup()
```

```python
# For rendering with PyOpenGL 
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

def renderScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 10,  # eye
              0, 0, 0,  # center
              0, 1, 0)  # up
    glEnable(GL_DEPTH_TEST)
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex3f(-10, -10, 0)
    glVertex3f(10, -10, 0)
    glVertex3f(10, 10, 0)
    glVertex3f(-10, 10, 0)
    glEnd()
    glutSwapBuffers()
```
