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
// ElevatorSimulator.js

/**
 * Elevator Simulator class
 * Demonstrates various design options and safety features of an elevator system
 */
class ElevatorSimulator {
  /**
   * Constructor
   * @param {number} numFloors - Number of floors in the building
   * @param {number} numElevators - Number of elevators in the building
   */
  constructor(numFloors, numElevators) {
    this.numFloors = numFloors;
    this.numElevators = numElevators;
    this.elevators = [];

    // Initialize elevators
    for (let i = 0; i < numElevators; i++) {
      this.elevators.push(new Elevator(i + 1, numFloors));
    }
  }

  /**
   * Start the elevator simulator
   */
  start() {
    console.log("Elevator simulator started.");

    // Start each elevator
    this.elevators.forEach((elevator) => {
      elevator.start();
    });
  }

  /**
   * Stop the elevator simulator
   */
  stop() {
    console.log("Elevator simulator stopped.");

    // Stop each elevator
    this.elevators.forEach((elevator) => {
      elevator.stop();
    });
  }

  /**
   * Request an elevator to move to a specific floor
   * @param {number} elevatorId - ID of the elevator to move
   * @param {number} floor - Floor to move to
   */
  requestElevator(elevatorId, floor) {
    const elevator = this.elevators.find((e) => e.id === elevatorId);

    if (elevator) {
      elevator.moveToFloor(floor);
    } else {
      console.error(`Elevator ${elevatorId} not found.`);
    }
  }
}

/**
 * Elevator class
 * Represents an individual elevator in the building
 */
class Elevator {
  /**
   * Constructor
   * @param {number} id - ID of the elevator
   * @param {number} numFloors - Number of floors in the building
   */
  constructor(id, numFloors) {
    this.id = id;
    this.numFloors = numFloors;
    this.currentFloor = 1;
    this.isMoving = false;
    this.isDoorOpen = false;
  }

  /**
   * Start the elevator
   */
  start() {
    console.log(`Elevator ${this.id} started.`);
  }

  /**
   * Stop the elevator
   */
  stop() {
    console.log(`Elevator ${this.id} stopped.`);
  }

  /**
   * Move the elevator to a specific floor
   * @param {number} floor - Floor to move to
   */
  moveToFloor(floor) {
    if (floor < 1 || floor > this.numFloors) {
      console.error(`Invalid floor ${floor}.`);
      return;
    }

    if (this.isMoving) {
      console.log(`Elevator ${this.id} is already moving.`);
      return;
    }

    this.isMoving = true;

    // Simulate movement
    const intervalId = setInterval(() => {
      if (this.currentFloor < floor) {
        this.currentFloor++;
      } else if (this.currentFloor > floor) {
        this.currentFloor--;
      } else {
        clearInterval(intervalId);
        this.isMoving = false;
        this.openDoor();
      }

      console.log(`Elevator ${this.id} is on floor ${this.currentFloor}.`);
    }, 1000); // Move one floor per second
  }

  /**
   * Open the elevator door
   */
  openDoor() {
    if (this.isDoorOpen) {
      console.log(`Elevator ${this.id} door is already open.`);
      return;
    }

    this.isDoorOpen = true;
    console.log(`Elevator ${this.id} door opened.`);
  }

  /**
   * Close the elevator door
   */
  closeDoor() {
    if (!this.isDoorOpen) {
      console.log(`Elevator ${this.id} door is already closed.`);
      return;
    }

    this.isDoorOpen = false;
    console.log(`Elevator ${this.id} door closed.`);
  }
}

// Example usage
const simulator = new ElevatorSimulator(10, 2);
simulator.start();

simulator.requestElevator(1, 5);
simulator.requestElevator(2, 8);

// Stop the simulator after 30 seconds
setTimeout(() => {
  simulator.stop();
}, 30000);
```
