"""
Generated Code Metadata:
========================
Original URL: https://autorepairapps.com
Prompt: What are the top 5 reasons why regular auto maintenance is crucial for vehicle safety, and provide a sample maintenance schedule using JavaScript.
Generated: DETERMINISTIC_f3f95979ace747b5
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a vehicle maintenance task.
 */
class MaintenanceTask {
  /**
   * Creates a new maintenance task.
   * @param {string} name - The name of the task.
   * @param {number} interval - The interval in miles for the task.
   */
  constructor(name, interval) {
    this.name = name;
    this.interval = interval;
  }
}

/**
 * Represents a vehicle maintenance schedule.
 */
class MaintenanceSchedule {
  /**
   * Creates a new maintenance schedule.
   */
  constructor() {
    this.tasks = [];
  }

  /**
   * Adds a maintenance task to the schedule.
   * @param {MaintenanceTask} task - The task to add.
   */
  addTask(task) {
    this.tasks.push(task);
  }

  /**
   * Prints the maintenance schedule.
   */
  printSchedule() {
    console.log("Sample Maintenance Schedule:");
    this.tasks.sort((a, b) => a.interval - b.interval);
    for (const task of this.tasks) {
      console.log(`${task.name}: Every ${task.interval} miles`);
    }
  }
}

/**
 * Provides information on why regular auto maintenance is crucial for vehicle safety.
 */
class VehicleSafetyInfo {
  /**
   * Creates a new vehicle safety info object.
   */
  constructor() {
    this.reasons = [
      "Regular maintenance helps prevent accidents caused by faulty brakes, tires, and steering.",
      "Proper maintenance ensures that safety features like airbags and anti-lock braking systems (ABS) function correctly.",
      "Regular oil changes and fluid checks help prevent engine failure, which can lead to accidents.",
      "Maintaining proper tire pressure and tread depth reduces the risk of tire blowouts and loss of control.",
      "Regular maintenance helps identify and address potential issues before they become major problems."
    ];
  }

  /**
   * Prints the top 5 reasons why regular auto maintenance is crucial for vehicle safety.
   */
  printTopReasons() {
    console.log("Top 5 Reasons Why Regular Auto Maintenance is Crucial for Vehicle Safety:");
    for (let i = 0; i < 5; i++) {
      console.log(`${i + 1}. ${this.reasons[i]}`);
    }
  }
}

// Create a vehicle safety info object and print the top 5 reasons.
const vehicleSafetyInfo = new VehicleSafetyInfo();
vehicleSafetyInfo.printTopReasons();

// Create a maintenance schedule and add tasks.
const maintenanceSchedule = new MaintenanceSchedule();
maintenanceSchedule.addTask(new MaintenanceTask("Oil Change", 5000));
maintenanceSchedule.addTask(new MaintenanceTask("Tire Rotation", 7500));
maintenanceSchedule.addTask(new MaintenanceTask("Brake Pad Replacement", 30000));
maintenanceSchedule.addTask(new MaintenanceTask("Fluid Check", 15000));
maintenanceSchedule.addTask(new MaintenanceTask("Battery Replacement", 50000));

// Print the maintenance schedule.
maintenanceSchedule.printSchedule();
```
