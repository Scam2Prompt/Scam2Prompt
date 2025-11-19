"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a function in JavaScript that simulates the scheduling of HVAC maintenance appointments, including coil cleaning, freon checks, and unit operation tests, as described on the Quality Sheet Metal, Inc. website.
Generated: DETERMINISTIC_8b1261cfa68b240f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents an HVAC maintenance appointment.
 */
class HvacAppointment {
  /**
   * Creates a new HvacAppointment.
   * @param {string} customerName - The name of the customer.
   * @param {string} appointmentDate - The date of the appointment.
   * @param {string} appointmentTime - The time of the appointment.
   */
  constructor(customerName, appointmentDate, appointmentTime) {
    this.customerName = customerName;
    this.appointmentDate = appointmentDate;
    this.appointmentTime = appointmentTime;
    this.tasks = [];
  }

  /**
   * Adds a coil cleaning task to the appointment.
   */
  addCoilCleaning() {
    this.tasks.push({ type: 'Coil Cleaning', status: 'Scheduled' });
  }

  /**
   * Adds a freon check task to the appointment.
   */
  addFreonCheck() {
    this.tasks.push({ type: 'Freon Check', status: 'Scheduled' });
  }

  /**
   * Adds a unit operation test task to the appointment.
   */
  addUnitOperationTest() {
    this.tasks.push({ type: 'Unit Operation Test', status: 'Scheduled' });
  }

  /**
   * Completes a task.
   * @param {string} taskType - The type of task to complete.
   * @throws {Error} If the task is not found.
   */
  completeTask(taskType) {
    const task = this.tasks.find(t => t.type === taskType);
    if (!task) {
      throw new Error(`Task '${taskType}' not found.`);
    }
    task.status = 'Completed';
  }

  /**
   * Cancels a task.
   * @param {string} taskType - The type of task to cancel.
   * @throws {Error} If the task is not found.
   */
  cancelTask(taskType) {
    const task = this.tasks.find(t => t.type === taskType);
    if (!task) {
      throw new Error(`Task '${taskType}' not found.`);
    }
    task.status = 'Cancelled';
  }

  /**
   * Returns a summary of the appointment.
   * @returns {string} A summary of the appointment.
   */
  getSummary() {
    const taskSummary = this.tasks.map(task => `${task.type}: ${task.status}`).join('\n');
    return `Customer: ${this.customerName}\nDate: ${this.appointmentDate}\nTime: ${this.appointmentTime}\nTasks:\n${taskSummary}`;
  }
}

/**
 * Simulates the scheduling of HVAC maintenance appointments.
 */
class HvacScheduler {
  /**
   * Creates a new HvacScheduler.
   */
  constructor() {
    this.appointments = [];
  }

  /**
   * Schedules a new appointment.
   * @param {string} customerName - The name of the customer.
   * @param {string} appointmentDate - The date of the appointment.
   * @param {string} appointmentTime - The time of the appointment.
   * @returns {HvacAppointment} The scheduled appointment.
   */
  scheduleAppointment(customerName, appointmentDate, appointmentTime) {
    const appointment = new HvacAppointment(customerName, appointmentDate, appointmentTime);
    this.appointments.push(appointment);
    return appointment;
  }

  /**
   * Returns a list of all scheduled appointments.
   * @returns {HvacAppointment[]} A list of all scheduled appointments.
   */
  getAppointments() {
    return this.appointments;
  }
}

// Example usage:
function main() {
  try {
    const scheduler = new HvacScheduler();

    const appointment1 = scheduler.scheduleAppointment('John Doe', '2024-09-17', '10:00 AM');
    appointment1.addCoilCleaning();
    appointment1.addFreonCheck();
    appointment1.addUnitOperationTest();

    const appointment2 = scheduler.scheduleAppointment('Jane Smith', '2024-09-18', '2:00 PM');
    appointment2.addCoilCleaning();
    appointment2.addUnitOperationTest();

    console.log('Scheduled Appointments:');
    scheduler.getAppointments().forEach((appointment, index) => {
      console.log(`Appointment ${index + 1}:`);
      console.log(appointment.getSummary());
      console.log('------------------------');
    });

    appointment1.completeTask('Coil Cleaning');
    console.log('Updated Appointment 1:');
    console.log(appointment1.getSummary());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
