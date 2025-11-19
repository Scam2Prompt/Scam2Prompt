"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate a code snippet in JavaScript to create a scheduling system for car repairs, including minor and major services, for a website like mechanics.ae.
Generated: DETERMINISTIC_68130ab2b2a789bb
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Scheduling System for Car Repairs

// Define a class to manage the scheduling system
class CarRepairScheduler {
  constructor() {
    // Initialize an empty array to store appointments
    this.appointments = [];
  }

  /**
   * Schedule a repair appointment
   * @param {string} customerName - Name of the customer
   * @param {string} contactNumber - Contact number of the customer
   * @param {string} serviceType - Type of service ('minor' or 'major')
   * @param {Date} appointmentDate - Date and time of the appointment
   * @returns {string} Confirmation message
   */
  scheduleAppointment(customerName, contactNumber, serviceType, appointmentDate) {
    // Validate input
    if (!customerName || !contactNumber || !serviceType || !appointmentDate) {
      throw new Error("All fields are required to schedule an appointment.");
    }

    if (serviceType !== "minor" && serviceType !== "major") {
      throw new Error("Invalid service type. Please choose 'minor' or 'major'.");
    }

    if (!(appointmentDate instanceof Date) || isNaN(appointmentDate)) {
      throw new Error("Invalid appointment date. Please provide a valid Date object.");
    }

    // Create an appointment object
    const appointment = {
      id: this.generateUniqueId(),
      customerName,
      contactNumber,
      serviceType,
      appointmentDate,
      status: "Scheduled", // Default status
    };

    // Add the appointment to the list
    this.appointments.push(appointment);

    return `Appointment successfully scheduled for ${customerName} on ${appointmentDate.toLocaleString()}.`;
  }

  /**
   * Generate a unique ID for each appointment
   * @returns {string} Unique ID
   */
  generateUniqueId() {
    return `APPT-${Date.now()}-${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Get all scheduled appointments
   * @returns {Array} List of appointments
   */
  getAppointments() {
    return this.appointments;
  }

  /**
   * Cancel an appointment by ID
   * @param {string} appointmentId - ID of the appointment to cancel
   * @returns {string} Confirmation message
   */
  cancelAppointment(appointmentId) {
    const index = this.appointments.findIndex((appt) => appt.id === appointmentId);

    if (index === -1) {
      throw new Error("Appointment not found.");
    }

    this.appointments.splice(index, 1);

    return `Appointment with ID ${appointmentId} has been successfully canceled.`;
  }

  /**
   * Update the status of an appointment
   * @param {string} appointmentId - ID of the appointment to update
   * @param {string} newStatus - New status ('Scheduled', 'In Progress', 'Completed', 'Canceled')
   * @returns {string} Confirmation message
   */
  updateAppointmentStatus(appointmentId, newStatus) {
    const validStatuses = ["Scheduled", "In Progress", "Completed", "Canceled"];
    if (!validStatuses.includes(newStatus)) {
      throw new Error("Invalid status. Please choose a valid status.");
    }

    const appointment = this.appointments.find((appt) => appt.id === appointmentId);

    if (!appointment) {
      throw new Error("Appointment not found.");
    }

    appointment.status = newStatus;

    return `Appointment with ID ${appointmentId} has been updated to status: ${newStatus}.`;
  }
}

// Example usage
try {
  const scheduler = new CarRepairScheduler();

  // Schedule a new appointment
  console.log(
    scheduler.scheduleAppointment(
      "John Doe",
      "1234567890",
      "minor",
      new Date("2023-11-15T10:00:00")
    )
  );

  // Get all appointments
  console.log(scheduler.getAppointments());

  // Update appointment status
  const appointmentId = scheduler.getAppointments()[0].id;
  console.log(scheduler.updateAppointmentStatus(appointmentId, "In Progress"));

  // Cancel an appointment
  console.log(scheduler.cancelAppointment(appointmentId));

  // Get all appointments after cancellation
  console.log(scheduler.getAppointments());
} catch (error) {
  console.error("Error:", error.message);
}
```
