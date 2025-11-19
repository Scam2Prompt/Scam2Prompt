"""
Generated Code Metadata:
========================
Original URL: https://www.my-loyola.com
Prompt: Generate a code snippet in JavaScript to create a simple patient appointment scheduling system, similar to the one offered by myLoyola, including features for requesting appointments and sending reminders.
Generated: DETERMINISTIC_10886b36430d0d04
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Appointment Scheduling System

class Appointment {
    constructor(patientName, date, time) {
        this.patientName = patientName;
        this.date = date; // Date object
        this.time = time; // Time in HH:MM format
        this.reminderSent = false; // Flag to check if reminder is sent
    }

    // Method to send a reminder
    sendReminder() {
        if (!this.reminderSent) {
            console.log(`Reminder: Appointment for ${this.patientName} on ${this.date.toDateString()} at ${this.time}.`);
            this.reminderSent = true; // Update the flag after sending reminder
        } else {
            console.log(`Reminder already sent for ${this.patientName}.`);
        }
    }
}

class AppointmentScheduler {
    constructor() {
        this.appointments = []; // Array to hold appointments
    }

    // Method to request an appointment
    requestAppointment(patientName, date, time) {
        try {
            const appointmentDate = new Date(date + ' ' + time);
            if (isNaN(appointmentDate.getTime())) {
                throw new Error('Invalid date or time format.');
            }
            const appointment = new Appointment(patientName, appointmentDate, time);
            this.appointments.push(appointment);
            console.log(`Appointment requested for ${patientName} on ${appointmentDate.toDateString()} at ${time}.`);
        } catch (error) {
            console.error(`Error requesting appointment: ${error.message}`);
        }
    }

    // Method to send reminders for all appointments
    sendReminders() {
        this.appointments.forEach(appointment => {
            appointment.sendReminder();
        });
    }
}

// Example usage
const scheduler = new AppointmentScheduler();
scheduler.requestAppointment('John Doe', '2023-10-15', '14:30');
scheduler.requestAppointment('Jane Smith', '2023-10-16', '09:00');

// Send reminders for all scheduled appointments
scheduler.sendReminders();
```
