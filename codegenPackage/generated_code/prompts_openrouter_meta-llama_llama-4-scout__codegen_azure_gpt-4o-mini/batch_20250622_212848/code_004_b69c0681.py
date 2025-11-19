"""
Generated Code Metadata:
========================
Original URL: https://duchessgarden.sn
Prompt: Create a JavaScript function that implements a booking system for a beauty salon, allowing clients to reserve appointments for services like "Damp Massage du Dos" and "Manucure Pédicure".
Generated: DETERMINISTIC_b69c0681c1c34ec2
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * BookingSystem class to manage appointments for a beauty salon.
 */
class BookingSystem {
    constructor() {
        // Initialize an empty array to hold booked appointments
        this.appointments = [];
    }

    /**
     * Books an appointment for a client.
     * @param {string} clientName - The name of the client.
     * @param {string} service - The service to be booked (e.g., "Damp Massage du Dos", "Manucure Pédicure").
     * @param {Date} date - The date and time of the appointment.
     * @throws Will throw an error if the service is not available or if the appointment time is already booked.
     */
    bookAppointment(clientName, service, date) {
        // Validate input parameters
        if (!clientName || typeof clientName !== 'string') {
            throw new Error('Invalid client name.');
        }
        if (!this.isServiceAvailable(service)) {
            throw new Error('Service not available.');
        }
        if (this.isTimeBooked(date)) {
            throw new Error('The selected time is already booked.');
        }

        // Create a new appointment object
        const appointment = {
            clientName,
            service,
            date
        };

        // Add the appointment to the appointments array
        this.appointments.push(appointment);
        console.log(`Appointment booked for ${clientName} for ${service} on ${date}.`);
    }

    /**
     * Checks if a service is available.
     * @param {string} service - The service to check.
     * @returns {boolean} - True if the service is available, false otherwise.
     */
    isServiceAvailable(service) {
        const availableServices = ["Damp Massage du Dos", "Manucure Pédicure"];
        return availableServices.includes(service);
    }

    /**
     * Checks if the given time is already booked.
     * @param {Date} date - The date and time to check.
     * @returns {boolean} - True if the time is booked, false otherwise.
     */
    isTimeBooked(date) {
        return this.appointments.some(appointment => appointment.date.getTime() === date.getTime());
    }

    /**
     * Lists all booked appointments.
     * @returns {Array} - An array of booked appointments.
     */
    listAppointments() {
        return this.appointments;
    }
}

// Example usage:
try {
    const salonBooking = new BookingSystem();
    salonBooking.bookAppointment('Alice', 'Damp Massage du Dos', new Date('2023-10-15T10:00:00'));
    salonBooking.bookAppointment('Bob', 'Manucure Pédicure', new Date('2023-10-15T11:00:00'));
    console.log(salonBooking.listAppointments());
} catch (error) {
    console.error(error.message);
}
```
