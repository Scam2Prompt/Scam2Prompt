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
/**
 * Car Repair Scheduling System
 * 
 * This module provides functionality to schedule car repair services,
 * including minor and major services, for a mechanics website.
 */

class CarRepairScheduler {
    /**
     * Initialize the scheduler with available services and time slots
     */
    constructor() {
        this.services = {
            minor: [
                { id: 1, name: 'Oil Change', duration: 30, price: 50 },
                { id: 2, name: 'Tire Rotation', duration: 45, price: 40 },
                { id: 3, name: 'Brake Inspection', duration: 60, price: 75 }
            ],
            major: [
                { id: 4, name: 'Engine Tune-Up', duration: 120, price: 200 },
                { id: 5, name: 'Transmission Service', duration: 180, price: 350 },
                { id: 6, name: 'Complete Brake Service', duration: 150, price: 300 }
            ]
        };

        this.availableSlots = this.generateTimeSlots();
        this.bookings = [];
    }

    /**
     * Generate time slots for the next 7 days
     * @returns {Array} Array of available time slots
     */
    generateTimeSlots() {
        const slots = [];
        const now = new Date();
        const daysToAdd = 7;
        const startHour = 8;
        const endHour = 18;
        const slotDuration = 30; // minutes

        for (let day = 0; day < daysToAdd; day++) {
            const currentDate = new Date(now);
            currentDate.setDate(now.getDate() + day);
            currentDate.setHours(startHour, 0, 0, 0);

            while (currentDate.getHours() < endHour) {
                const slotEnd = new Date(currentDate);
                slotEnd.setMinutes(currentDate.getMinutes() + slotDuration);

                slots.push({
                    date: new Date(currentDate),
                    endTime: new Date(slotEnd),
                    isBooked: false
                });

                currentDate.setMinutes(currentDate.getMinutes() + slotDuration);
            }
        }

        return slots;
    }

    /**
     * Get available services by type
     * @param {string} type - 'minor' or 'major'
     * @returns {Array} Array of services
     */
    getServices(type) {
        if (!this.services[type]) {
            throw new Error(`Invalid service type: ${type}. Must be 'minor' or 'major'`);
        }
        return this.services[type];
    }

    /**
     * Get available time slots
     * @param {Date} date - Optional date filter
     * @returns {Array} Array of available slots
     */
    getAvailableSlots(date = null) {
        if (date) {
            const filterDate = new Date(date);
            filterDate.setHours(0, 0, 0, 0);
            return this.availableSlots.filter(slot => 
                !slot.isBooked && 
                slot.date.getDate() === filterDate.getDate() &&
                slot.date.getMonth() === filterDate.getMonth() &&
                slot.date.getFullYear() === filterDate.getFullYear()
            );
        }
        return this.availableSlots.filter(slot => !slot.isBooked);
    }

    /**
     * Book a service appointment
     * @param {number} serviceId - ID of the service to book
     * @param {Date} slot - Time slot to book
     * @param {Object} customerInfo - Customer information
     * @returns {Object} Booking confirmation
     */
    bookAppointment(serviceId, slot, customerInfo) {
        // Validate inputs
        if (!serviceId || !slot || !customerInfo || !customerInfo.name || !customerInfo.phone) {
            throw new Error('Missing required booking information');
        }

        // Find the service
        let service;
        for (const type in this.services) {
            const found = this.services[type].find(s => s.id === serviceId);
            if (found) {
                service = found;
                break;
            }
        }

        if (!service) {
            throw new Error(`Service with ID ${serviceId} not found`);
        }

        // Find and validate the slot
        const foundSlot = this.availableSlots.find(s => 
            s.date.getTime() === slot.getTime() && 
            !s.isBooked
        );

        if (!foundSlot) {
            throw new Error('Selected time slot is not available');
        }

        // Check if slot duration is sufficient
        const slotDuration = (foundSlot.endTime - foundSlot.date) / (1000 * 60);
        if (slotDuration < service.duration) {
            throw new Error(`Selected slot duration (${slotDuration}min) is insufficient for service (${service.duration}min)`);
        }

        // Mark slot as booked
        foundSlot.isBooked = true;

        // Create booking
        const booking = {
            id: this.bookings.length + 1,
            service,
            slot: foundSlot,
            customerInfo,
            bookingDate: new Date(),
            status: 'confirmed'
        };

        this.bookings.push(booking);

        return {
            success: true,
            bookingId: booking.id,
            message: 'Appointment booked successfully'
        };
    }

    /**
     * Cancel an existing booking
     * @param {number} bookingId - ID of the booking to cancel
     * @returns {Object} Cancellation confirmation
     */
    cancelBooking(bookingId) {
        const bookingIndex = this.bookings.findIndex(b => b.id === bookingId);
        
        if (bookingIndex === -1) {
            throw new Error(`Booking with ID ${bookingId} not found`);
        }

        const booking = this.bookings[bookingIndex];

        // Free up the time slot
        const slot = this.availableSlots.find(s => 
            s.date.getTime() === booking.slot.date.getTime()
        );
        
        if (slot) {
            slot.isBooked = false;
        }

        // Update booking status
        booking.status = 'cancelled';

        return {
            success: true,
            message: 'Booking cancelled successfully'
        };
    }
}

// Example usage:
// const scheduler = new CarRepairScheduler();
// const availableServices = scheduler.getServices('minor');
// const availableSlots = scheduler.getAvailableSlots();
// const booking = scheduler.bookAppointment(1, availableSlots[0], {
//     name: 'John Doe',
//     phone: '+971501234567',
//     carModel: 'Toyota Camry'
// });
// const cancellation = scheduler.cancelBooking(booking.bookingId);
```
