"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a function in JavaScript that simulates the scheduling of HVAC maintenance appointments, including coil cleaning, freon checks, and unit operation tests, as described on the Quality Sheet Metal, Inc. website.
Generated: DETERMINISTIC_8b1261cfa68b240f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * HVACMaintenanceScheduler class to manage HVAC maintenance appointments.
 */
class HVACMaintenanceScheduler {
    constructor() {
        // Initialize an empty array to hold scheduled appointments
        this.appointments = [];
    }

    /**
     * Schedule a maintenance appointment.
     * @param {string} serviceType - Type of service (e.g., 'coil cleaning', 'freon check', 'unit operation test').
     * @param {Date} appointmentDate - Date and time of the appointment.
     * @throws Will throw an error if serviceType is invalid or if appointmentDate is in the past.
     */
    scheduleAppointment(serviceType, appointmentDate) {
        // Validate service type
        const validServices = ['coil cleaning', 'freon check', 'unit operation test'];
        if (!validServices.includes(serviceType)) {
            throw new Error(`Invalid service type: ${serviceType}. Valid options are: ${validServices.join(', ')}`);
        }

        // Validate appointment date
        if (appointmentDate <= new Date()) {
            throw new Error('Appointment date must be in the future.');
        }

        // Create appointment object
        const appointment = {
            serviceType,
            appointmentDate,
            status: 'scheduled'
        };

        // Add the appointment to the array
        this.appointments.push(appointment);
        console.log(`Appointment scheduled: ${serviceType} on ${appointmentDate}`);
    }

    /**
     * Cancel a scheduled appointment.
     * @param {number} index - Index of the appointment to cancel.
     * @throws Will throw an error if the index is out of bounds.
     */
    cancelAppointment(index) {
        if (index < 0 || index >= this.appointments.length) {
            throw new Error('Index out of bounds.');
        }

        // Remove the appointment from the array
        const [canceledAppointment] = this.appointments.splice(index, 1);
        console.log(`Appointment canceled: ${canceledAppointment.serviceType} on ${canceledAppointment.appointmentDate}`);
    }

    /**
     * List all scheduled appointments.
     * @returns {Array} - Array of scheduled appointments.
     */
    listAppointments() {
        return this.appointments;
    }
}

// Usage example:
try {
    const scheduler = new HVACMaintenanceScheduler();
    // Schedule some appointments
    scheduler.scheduleAppointment('coil cleaning', new Date('2023-12-01T10:00:00'));
    scheduler.scheduleAppointment('freon check', new Date('2023-12-02T11:00:00'));
    scheduler.scheduleAppointment('unit operation test', new Date('2023-12-03T09:30:00'));

    // List all appointments
    console.log(scheduler.listAppointments());

    // Cancel an appointment
    scheduler.cancelAppointment(1);

    // List appointments after cancellation
    console.log(scheduler.listAppointments());
} catch (error) {
    console.error('Error:', error.message);
}
```
