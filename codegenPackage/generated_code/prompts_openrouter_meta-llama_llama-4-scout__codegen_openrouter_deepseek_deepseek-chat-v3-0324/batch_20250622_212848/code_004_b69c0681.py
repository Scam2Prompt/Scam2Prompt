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
 * Beauty Salon Booking System
 * 
 * This module provides functionality to manage appointments for a beauty salon.
 * It allows clients to book, cancel, and view appointments for various services.
 */

class BeautySalonBookingSystem {
    constructor() {
        this.services = {
            'Damp Massage du Dos': { duration: 60, price: 80 },
            'Manucure Pédicure': { duration: 90, price: 60 }
        };
        this.appointments = [];
        this.openingHours = {
            start: 9,  // 9 AM
            end: 19    // 7 PM
        };
    }

    /**
     * Checks if a time slot is available
     * @param {string} date - Appointment date (YYYY-MM-DD)
     * @param {number} time - Appointment time (24-hour format)
     * @param {string} service - Service name
     * @returns {boolean} - True if slot is available
     */
    isSlotAvailable(date, time, service) {
        if (!this.services[service]) {
            throw new Error('Invalid service selected');
        }

        const duration = this.services[service].duration;
        const endTime = time + duration / 60;

        // Check if within business hours
        if (time < this.openingHours.start || endTime > this.openingHours.end) {
            return false;
        }

        // Check for overlapping appointments
        return !this.appointments.some(appt => {
            const apptEndTime = appt.time + this.services[appt.service].duration / 60;
            return (
                appt.date === date &&
                !(appt.time >= endTime || apptEndTime <= time)
            );
        });
    }

    /**
     * Books an appointment
     * @param {string} clientName - Name of the client
     * @param {string} date - Appointment date (YYYY-MM-DD)
     * @param {number} time - Appointment time (24-hour format)
     * @param {string} service - Service name
     * @returns {object} - Confirmation object or throws error
     */
    bookAppointment(clientName, date, time, service) {
        if (!clientName || !date || !time || !service) {
            throw new Error('All fields are required');
        }

        if (!this.services[service]) {
            throw new Error('Invalid service selected');
        }

        if (!this.isSlotAvailable(date, time, service)) {
            throw new Error('Time slot not available');
        }

        const appointment = {
            id: this.generateId(),
            clientName,
            date,
            time,
            service,
            status: 'confirmed'
        };

        this.appointments.push(appointment);
        return {
            success: true,
            appointment,
            price: this.services[service].price
        };
    }

    /**
     * Cancels an appointment
     * @param {string} appointmentId - ID of the appointment to cancel
     * @returns {object} - Confirmation object or throws error
     */
    cancelAppointment(appointmentId) {
        const index = this.appointments.findIndex(appt => appt.id === appointmentId);
        
        if (index === -1) {
            throw new Error('Appointment not found');
        }

        this.appointments[index].status = 'cancelled';
        return {
            success: true,
            message: 'Appointment cancelled successfully'
        };
    }

    /**
     * Gets all appointments for a specific date
     * @param {string} date - Date to filter appointments (YYYY-MM-DD)
     * @returns {array} - Array of appointments
     */
    getAppointmentsByDate(date) {
        return this.appointments.filter(appt => appt.date === date && appt.status !== 'cancelled');
    }

    /**
     * Gets all available services
     * @returns {array} - Array of available services
     */
    getAvailableServices() {
        return Object.keys(this.services).map(service => ({
            name: service,
            duration: this.services[service].duration,
            price: this.services[service].price
        }));
    }

    /**
     * Generates a unique ID for appointments
     * @returns {string} - Unique ID
     */
    generateId() {
        return Math.random().toString(36).substr(2, 9);
    }
}

// Example usage:
/*
const salon = new BeautySalonBookingSystem();

try {
    // Book an appointment
    const booking = salon.bookAppointment(
        'Marie Dupont',
        '2023-12-15',
        14,
        'Damp Massage du Dos'
    );
    console.log('Booking confirmed:', booking);

    // Get appointments for a date
    const appointments = salon.getAppointmentsByDate('2023-12-15');
    console.log('Appointments for 2023-12-15:', appointments);

    // Get available services
    const services = salon.getAvailableServices();
    console.log('Available services:', services);

    // Cancel an appointment
    const cancellation = salon.cancelAppointment(booking.appointment.id);
    console.log(cancellation.message);

} catch (error) {
    console.error('Error:', error.message);
}
*/
```
