"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: Generate a code snippet that simulates the multi-robot coordination feature of BellaBot, allowing up to 20 robots to operate simultaneously in a restaurant setting.
Generated: DETERMINISTIC_bb56cfd8726dd0c1
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
import random
from queue import Queue
from typing import Dict, List, Optional

class Robot:
    def __init__(self, robot_id: int):
        self.id = robot_id
        self.current_task: Optional[str] = None
        self.battery_level = 100
        self.position = (0, 0)  # (x, y) coordinates
        self.is_active = True
        self.task_queue = Queue()
        self.lock = threading.Lock()

    def update_battery(self, consumption: int):
        with self.lock:
            self.battery_level -= consumption
            if self.battery_level <= 20:
                self.return_to_charging_station()

    def return_to_charging_station(self):
        with self.lock:
            self.current_task = "Returning to charging station"
            self.position = (0, 0)  # Assuming (0,0) is charging station
            self.battery_level = 100
            self.is_active = True

    def assign_task(self, task: str):
        with self.lock:
            if self.is_active:
                self.task_queue.put(task)
                return True
        return False

    def execute_task(self):
        while True:
            if not self.task_queue.empty():
                with self.lock:
                    if not self.is_active:
                        continue
                    self.current_task = self.task_queue.get()
                
                # Simulate task execution
                task_duration = random.randint(1, 5)
                time.sleep(task_duration)
                
                # Update battery after task
                self.update_battery(random.randint(5, 15))
                
                with self.lock:
                    self.current_task = None
            else:
                time.sleep(0.1)

class RestaurantMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.obstacles = set()
        self.tables = {}
        self.charging_station = (0, 0)
        
    def add_obstacle(self, x: int, y: int):
        self.obstacles.add((x, y))
        
    def add_table(self, table_id: int, x: int, y: int):
        self.tables[table_id] = (x, y)
        
    def is_valid_position(self, x: int, y: int) -> bool:
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                (x, y) not in self.obstacles)

class MultiRobotCoordinator:
    def __init__(self, num_robots: int = 20):
        if num_robots > 20:
            raise ValueError("Maximum 20 robots supported")
            
        self.robots: Dict[int, Robot] = {}
        self.restaurant_map = RestaurantMap(20, 20)
        self.task_list = [
            "Deliver food", "Clear table", "Assist customer",
            "Transport dishes", "Guide customers"
        ]
        
        # Initialize robots
        for i in range(num_robots):
            self.robots[i] = Robot(i)
            threading.Thread(
                target=self.robots[i].execute_task,
                daemon=True
            ).start()
        
        # Initialize restaurant map
        self._initialize_map()
        
    def _initialize_map(self):
        # Add some obstacles
        for _ in range(10):
            x, y = random.randint(1, 19), random.randint(1, 19)
            self.restaurant_map.add_obstacle(x, y)
            
        # Add tables
        for i in range(1, 21):
            while True:
                x, y = random.randint(1, 19), random.randint(1, 19)
                if (x, y) not in self.restaurant_map.obstacles:
                    self.restaurant_map.add_table(i, x, y)
                    break
    
    def assign_random_task(self):
        available_robots = [
            r for r in self.robots.values() 
            if r.is_active and r.current_task is None
        ]
        
        if not available_robots:
            return False
            
        robot = random.choice(available_robots)
        task = random.choice(self.task_list)
        return robot.assign_task(task)
    
    def get_robot_status(self, robot_id: int) -> Dict:
        robot = self.robots.get(robot_id)
        if not robot:
            return {}
            
        return {
            "id": robot.id,
            "current_task": robot.current_task,
            "battery_level": robot.battery_level,
            "position": robot.position,
            "is_active": robot.is_active
        }
    
    def get_all_robots_status(self) -> List[Dict]:
        return [self.get_robot_status(rid) for rid in self.robots.keys()]

def main():
    coordinator = MultiRobotCoordinator(num_robots=20)
    
    try:
        while True:
            # Assign random tasks to robots
            for _ in range(5):
                coordinator.assign_random_task()
            
            # Print status of all robots
            print("\nCurrent Robot Status:")
            for status in coordinator.get_all_robots_status():
                print(f"Robot {status['id']}: {status['current_task'] or 'Idle'}, "
                      f"Battery: {status['battery_level']}%, "
                      f"Position: {status['position']}")
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nShutting down robot coordination system...")

if __name__ == "__main__":
    main()
```
