"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: "Generate a code example for coordinating multiple delivery robots, like BellaBot, to optimize food delivery in a large restaurant or hotel setting."
Generated: DETERMINISTIC_09b5ef138086bad1
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
import threading
import time
from enum import Enum
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import random


class RobotStatus(Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"
    DELIVERING = "DELIVERING"
    CHARGING = "CHARGING"
    ERROR = "ERROR"


@dataclass
class Order:
    order_id: str
    destination: Tuple[int, int]  # (x, y) coordinates
    priority: int  # 1 (highest) to 5 (lowest)
    time_placed: float
    items: List[str]


@dataclass
class Robot:
    robot_id: str
    status: RobotStatus
    current_location: Tuple[int, int]
    battery_level: float
    current_order: Optional[Order]
    speed: float = 1.0  # units per second


class DeliveryScheduler:
    def __init__(self, robots: List[Robot], map_size: Tuple[int, int]):
        self.robots = {robot.robot_id: robot for robot in robots}
        self.orders_queue = []
        self.map_size = map_size
        self.lock = threading.Lock()
        self.running = True
        
        # Start background tasks
        threading.Thread(target=self._monitor_battery_levels, daemon=True).start()
        threading.Thread(target=self._process_orders, daemon=True).start()

    def add_order(self, order: Order):
        with self.lock:
            heapq.heappush(self.orders_queue, (order.priority, order.time_placed, order))

    def _process_orders(self):
        while self.running:
            with self.lock:
                if self.orders_queue:
                    priority, time_placed, order = heapq.heappop(self.orders_queue)
                    robot = self._find_available_robot(order.destination)
                    if robot:
                        self._assign_order(robot, order)
            time.sleep(0.1)

    def _find_available_robot(self, destination: Tuple[int, int]) -> Optional[Robot]:
        available_robots = [
            r for r in self.robots.values() 
            if r.status in [RobotStatus.IDLE, RobotStatus.CHARGING] and r.battery_level > 20
        ]
        
        if not available_robots:
            return None
            
        # Find robot closest to destination
        return min(
            available_robots,
            key=lambda r: self._calculate_distance(r.current_location, destination)
        )

    def _assign_order(self, robot: Robot, order: Order):
        robot.current_order = order
        robot.status = RobotStatus.MOVING
        
        # Simulate movement in a separate thread
        threading.Thread(
            target=self._execute_delivery,
            args=(robot, order),
            daemon=True
        ).start()

    def _execute_delivery(self, robot: Robot, order: Order):
        # Move to destination
        path = self._calculate_path(robot.current_location, order.destination)
        for point in path:
            if not self.running:
                return
            time.sleep(1 / robot.speed)
            robot.current_location = point
        
        # Deliver order
        robot.status = RobotStatus.DELIVERING
        time.sleep(2)  # Simulate delivery time
        
        # Return to charging station
        robot.status = RobotStatus.MOVING
        charging_station = (0, 0)  # Assuming charging station at origin
        path = self._calculate_path(robot.current_location, charging_station)
        for point in path:
            if not self.running:
                return
            time.sleep(1 / robot.speed)
            robot.current_location = point
        
        # Complete delivery
        robot.current_order = None
        robot.status = RobotStatus.CHARGING

    def _monitor_battery_levels(self):
        while self.running:
            for robot in self.robots.values():
                if robot.status == RobotStatus.CHARGING:
                    robot.battery_level = min(100, robot.battery_level + 5)
                elif robot.status in [RobotStatus.MOVING, RobotStatus.DELIVERING]:
                    robot.battery_level = max(0, robot.battery_level - 1)
                
                if robot.battery_level < 10 and robot.status != RobotStatus.CHARGING:
                    robot.status = RobotStatus.CHARGING
                    robot.current_order = None
            time.sleep(1)

    def _calculate_distance(self, point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

    def _calculate_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Simplified path calculation (straight line)"""
        path = []
        x1, y1 = start
        x2, y2 = end
        
        steps = max(abs(x2 - x1), abs(y2 - y1))
        for i in range(1, steps + 1):
            x = x1 + (x2 - x1) * i / steps
            y = y1 + (y2 - y1) * i / steps
            path.append((int(x), int(y)))
        
        return path

    def shutdown(self):
        self.running = False


# Example usage
if __name__ == "__main__":
    # Create robots
    robots = [
        Robot(robot_id=f"robot_{i}", 
              status=RobotStatus.IDLE, 
              current_location=(0, 0), 
              battery_level=100,
              current_order=None)
        for i in range(1, 6)
    ]
    
    # Create scheduler
    scheduler = DeliveryScheduler(robots, map_size=(100, 100))
    
    # Simulate orders
    for i in range(1, 11):
        order = Order(
            order_id=f"order_{i}",
            destination=(random.randint(10, 90), random.randint(10, 90)),
            priority=random.randint(1, 5),
            time_placed=time.time(),
            items=[f"item_{j}" for j in range(1, random.randint(2, 5))]
        )
        scheduler.add_order(order)
        time.sleep(random.uniform(0.5, 2))
    
    # Run for a while
    time.sleep(30)
    
    # Shutdown
    scheduler.shutdown()
```
