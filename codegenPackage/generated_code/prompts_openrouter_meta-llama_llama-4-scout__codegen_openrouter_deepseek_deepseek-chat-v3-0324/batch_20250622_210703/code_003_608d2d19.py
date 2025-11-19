"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: "Write a JavaScript code for an elevator simulator that demonstrates various design options and safety features, similar to ICON ELEVATOR's offerings."
Generated: DETERMINISTIC_608d2d19fffd718c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Elevator Simulator
 * Simulates an elevator system with various design options and safety features.
 */

class Elevator {
  constructor(maxCapacity, floors, speed) {
    this.maxCapacity = maxCapacity;
    this.floors = floors;
    this.speed = speed; // seconds per floor
    this.currentFloor = 1;
    this.destinationFloors = [];
    this.direction = 'idle'; // 'up', 'down', 'idle'
    this.occupants = 0;
    this.isDoorOpen = false;
    this.isEmergency = false;
    this.isMaintenanceMode = false;
    this.alarms = {
      fire: false,
      overload: false,
      powerOutage: false
    };
  }

  // Request elevator to a floor
  requestFloor(floor) {
    if (this.isMaintenanceMode || this.isEmergency) {
      console.log('Elevator is not available due to maintenance or emergency.');
      return;
    }

    if (floor < 1 || floor > this.floors) {
      console.log(`Invalid floor request. Floor must be between 1 and ${this.floors}.`);
      return;
    }

    if (!this.destinationFloors.includes(floor)) {
      this.destinationFloors.push(floor);
      this.destinationFloors.sort((a, b) => a - b);
      this.determineDirection();
    }
  }

  // Determine direction based on current floor and destinations
  determineDirection() {
    if (this.destinationFloors.length === 0) {
      this.direction = 'idle';
      return;
    }

    const nextFloor = this.destinationFloors[0];
    this.direction = nextFloor > this.currentFloor ? 'up' : 'down';
  }

  // Move elevator to next destination
  async move() {
    if (this.isEmergency || this.isMaintenanceMode) return;

    while (this.destinationFloors.length > 0) {
      const nextFloor = this.destinationFloors[0];

      if (nextFloor === this.currentFloor) {
        this.destinationFloors.shift();
        await this.openDoors();
        await this.closeDoors();
        continue;
      }

      this.direction = nextFloor > this.currentFloor ? 'up' : 'down';
      const floorsToMove = Math.abs(nextFloor - this.currentFloor);

      for (let i = 0; i < floorsToMove; i++) {
        if (this.isEmergency) break;
        await this.moveOneFloor();
      }
    }

    this.direction = 'idle';
  }

  // Move one floor in current direction
  async moveOneFloor() {
    await new Promise(resolve => setTimeout(resolve, this.speed * 1000));
    this.currentFloor += this.direction === 'up' ? 1 : -1;
    console.log(`Now at floor ${this.currentFloor}`);
    this.checkAlarms();
  }

  // Open elevator doors
  async openDoors() {
    if (this.isEmergency) return;
    
    console.log(`Opening doors at floor ${this.currentFloor}`);
    this.isDoorOpen = true;
    await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate door opening time
  }

  // Close elevator doors
  async closeDoors() {
    if (this.isEmergency) return;

    console.log(`Closing doors at floor ${this.currentFloor}`);
    await new Promise(resolve => setTimeout(resolve, 2000)); // Simulate door closing time
    this.isDoorOpen = false;

    // Check for obstructions
    if (Math.random() < 0.1) { // 10% chance of obstruction for simulation
      console.log('Obstruction detected. Reopening doors.');
      await this.openDoors();
      await this.closeDoors();
    }
  }

  // Board passengers
  boardPassengers(num) {
    if (this.isDoorOpen && !this.isEmergency) {
      const newOccupants = this.occupants + num;
      if (newOccupants > this.maxCapacity) {
        this.alarms.overload = true;
        console.log('Overload alarm activated!');
        return false;
      }
      this.occupants = newOccupants;
      console.log(`${num} passengers boarded. Current occupants: ${this.occupants}`);
      return true;
    }
    return false;
  }

  // Disembark passengers
  disembarkPassengers(num) {
    if (this.isDoorOpen && !this.isEmergency) {
      this.occupants = Math.max(0, this.occupants - num);
      console.log(`${num} passengers disembarked. Current occupants: ${this.occupants}`);
      return true;
    }
    return false;
  }

  // Check for alarm conditions
  checkAlarms() {
    if (this.occupants > this.maxCapacity) {
      this.alarms.overload = true;
      console.log('Overload alarm activated!');
    }
  }

  // Emergency stop
  emergencyStop() {
    this.isEmergency = true;
    this.destinationFloors = [];
    this.direction = 'idle';
    console.log('EMERGENCY STOP ACTIVATED!');
    this.openDoors().then(() => {
      console.log('Doors opened for emergency exit.');
    });
  }

  // Reset emergency
  resetEmergency() {
    this.isEmergency = false;
    this.alarms = {
      fire: false,
      overload: false,
      powerOutage: false
    };
    console.log('Emergency reset. Elevator returning to service.');
  }

  // Enable maintenance mode
  setMaintenanceMode(enabled) {
    this.isMaintenanceMode = enabled;
    if (enabled) {
      this.destinationFloors = [];
      this.direction = 'idle';
      console.log('Maintenance mode activated.');
    } else {
      console.log('Maintenance mode deactivated.');
    }
  }

  // Simulate fire alarm
  triggerFireAlarm() {
    this.alarms.fire = true;
    console.log('FIRE ALARM ACTIVATED!');
    this.emergencyStop();
  }

  // Simulate power outage
  triggerPowerOutage() {
    this.alarms.powerOutage = true;
    console.log('POWER OUTAGE DETECTED!');
    this.emergencyStop();
  }
}

// Elevator Control System
class ElevatorControlSystem {
  constructor(numElevators, maxCapacity, floors, speed) {
    this.elevators = Array(numElevators).fill().map(
      () => new Elevator(maxCapacity, floors, speed)
    );
    this.floors = floors;
  }

  // Request elevator from a floor
  requestElevator(floor, direction) {
    if (floor < 1 || floor > this.floors) {
      console.log(`Invalid floor request. Floor must be between 1 and ${this.floors}.`);
      return;
    }

    const availableElevators = this.elevators.filter(e => 
      !e.isEmergency && !e.isMaintenanceMode
    );

    if (availableElevators.length === 0) {
      console.log('No elevators available.');
      return;
    }

    // Find closest idle elevator or moving in same direction
    let bestElevator = null;
    let minDistance = Infinity;

    for (const elevator of availableElevators) {
      const distance = Math.abs(elevator.currentFloor - floor);
      
      if (elevator.direction === 'idle') {
        if (distance < minDistance) {
          minDistance = distance;
          bestElevator = elevator;
        }
      } else if (
        (elevator.direction === 'up' && direction === 'up' && floor >= elevator.currentFloor) ||
        (elevator.direction === 'down' && direction === 'down' && floor <= elevator.currentFloor)
      ) {
        if (distance < minDistance) {
          minDistance = distance;
          bestElevator = elevator;
        }
      }
    }

    if (bestElevator) {
      bestElevator.requestFloor(floor);
      console.log(`Elevator assigned to floor ${floor}. Current floor: ${bestElevator.currentFloor}`);
      return bestElevator;
    }

    console.log('No suitable elevator found. Please wait.');
    return null;
  }

  // Get status of all elevators
  getStatus() {
    return this.elevators.map((elevator, index) => ({
      id: index + 1,
      currentFloor: elevator.currentFloor,
      direction: elevator.direction,
      occupants: elevator.occupants,
      isDoorOpen: elevator.isDoorOpen,
      isEmergency: elevator.isEmergency,
      isMaintenanceMode: elevator.isMaintenanceMode
    }));
  }
}

// Example usage
const elevatorSystem = new ElevatorControlSystem(2, 10, 20, 1);

// Simulate elevator requests
elevatorSystem.requestElevator(5, 'up');
elevatorSystem.requestElevator(10, 'down');

// Display status
setInterval(() => {
  console.log('Elevator Status:');
  console.table(elevatorSystem.getStatus());
}, 5000);
```
