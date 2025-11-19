"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Generate a code snippet in JavaScript to create a simple tennis court booking system, considering factors like court availability, time slots, and user reservations.
Generated: DETERMINISTIC_79605e3ae441b914
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tennis Court Booking System
 * 
 * Features:
 * - Manage court availability
 * - Handle time slot reservations
 * - User booking management
 */

class TennisCourtBookingSystem {
    /**
     * Initialize the booking system with courts and time slots
     * @param {number} courtCount - Number of available courts
     * @param {number} slotDuration - Duration of each time slot in minutes
     * @param {string} openingTime - Opening time in 'HH:MM' format
     * @param {string} closingTime - Closing time in 'HH:MM' format
     */
    constructor(courtCount = 2, slotDuration = 60, openingTime = '08:00', closingTime = '22:00') {
        this.courts = Array(courtCount).fill().map((_, i) => ({
            id: i + 1,
            bookings: new Map()
        }));
        
        this.slotDuration = slotDuration;
        this.openingTime = openingTime;
        this.closingTime = closingTime;
    }

    /**
     * Convert time string to minutes since midnight
     * @param {string} time - Time in 'HH:MM' format
     * @returns {number} Total minutes
     */
    _timeToMinutes(time) {
        const [hours, minutes] = time.split(':').map(Number);
        return hours * 60 + minutes;
    }

    /**
     * Generate all available time slots for a day
     * @returns {Array} Array of time slot strings in 'HH:MM' format
     */
    _generateTimeSlots() {
        const slots = [];
        const open = this._timeToMinutes(this.openingTime);
        const close = this._timeToMinutes(this.closingTime);
        
        for (let time = open; time + this.slotDuration <= close; time += this.slotDuration) {
            const hours = Math.floor(time / 60).toString().padStart(2, '0');
            const minutes = (time % 60).toString().padStart(2, '0');
            slots.push(`${hours}:${minutes}`);
        }
        
        return slots;
    }

    /**
     * Check if a time slot is valid
     * @param {string} time - Time slot to check
     * @returns {boolean} True if valid
     */
    _isValidTimeSlot(time) {
        const slots = this._generateTimeSlots();
        return slots.includes(time);
    }

    /**
     * Book a court
     * @param {number} courtId - Court number (1-based)
     * @param {string} timeSlot - Time slot in 'HH:MM' format
     * @param {string} userId - User identifier
     * @returns {Object} Booking result {success: boolean, message: string}
     */
    bookCourt(courtId, timeSlot, userId) {
        try {
            // Validate court ID
            if (courtId < 1 || courtId > this.courts.length) {
                return {success: false, message: 'Invalid court ID'};
            }

            // Validate time slot
            if (!this._isValidTimeSlot(timeSlot)) {
                return {success: false, message: 'Invalid time slot'};
            }

            const court = this.courts[courtId - 1];

            // Check availability
            if (court.bookings.has(timeSlot)) {
                return {success: false, message: 'Time slot already booked'};
            }

            // Create booking
            court.bookings.set(timeSlot, {
                userId,
                bookedAt: new Date()
            });

            return {success: true, message: 'Booking successful'};
        } catch (error) {
            console.error('Booking error:', error);
            return {success: false, message: 'An error occurred during booking'};
        }
    }

    /**
     * Cancel a booking
     * @param {number} courtId - Court number (1-based)
     * @param {string} timeSlot - Time slot in 'HH:MM' format
     * @param {string} userId - User identifier
     * @returns {Object} Cancellation result {success: boolean, message: string}
     */
    cancelBooking(courtId, timeSlot, userId) {
        try {
            // Validate court ID
            if (courtId < 1 || courtId > this.courts.length) {
                return {success: false, message: 'Invalid court ID'};
            }

            const court = this.courts[courtId - 1];

            // Check if booking exists
            if (!court.bookings.has(timeSlot)) {
                return {success: false, message: 'No booking found for this time slot'};
            }

            // Verify user owns the booking
            const booking = court.bookings.get(timeSlot);
            if (booking.userId !== userId) {
                return {success: false, message: 'You do not own this booking'};
            }

            // Cancel booking
            court.bookings.delete(timeSlot);
            return {success: true, message: 'Booking cancelled successfully'};
        } catch (error) {
            console.error('Cancellation error:', error);
            return {success: false, message: 'An error occurred during cancellation'};
        }
    }

    /**
     * Get available time slots for a court
     * @param {number} courtId - Court number (1-based)
     * @returns {Object} Result {success: boolean, data: Array, message: string}
     */
    getAvailableSlots(courtId) {
        try {
            // Validate court ID
            if (courtId < 1 || courtId > this.courts.length) {
                return {success: false, data: null, message: 'Invalid court ID'};
            }

            const allSlots = this._generateTimeSlots();
            const court = this.courts[courtId - 1];
            const availableSlots = allSlots.filter(slot => !court.bookings.has(slot));

            return {success: true, data: availableSlots, message: 'Available slots retrieved'};
        } catch (error) {
            console.error('Availability check error:', error);
            return {success: false, data: null, message: 'An error occurred while checking availability'};
        }
    }

    /**
     * Get all bookings for a user
     * @param {string} userId - User identifier
     * @returns {Object} Result {success: boolean, data: Array, message: string}
     */
    getUserBookings(userId) {
        try {
            const userBookings = [];

            this.courts.forEach(court => {
                court.bookings.forEach((booking, timeSlot) => {
                    if (booking.userId === userId) {
                        userBookings.push({
                            courtId: court.id,
                            timeSlot,
                            bookedAt: booking.bookedAt
                        });
                    }
                });
            });

            return {success: true, data: userBookings, message: 'User bookings retrieved'};
        } catch (error) {
            console.error('User bookings error:', error);
            return {success: false, data: null, message: 'An error occurred while retrieving user bookings'};
        }
    }
}

// Example usage:
// const bookingSystem = new TennisCourtBookingSystem();
// const bookingResult = bookingSystem.bookCourt(1, '10:00', 'user123');
// const availableSlots = bookingSystem.getAvailableSlots(1);
// const userBookings = bookingSystem.getUserBookings('user123');
// const cancelResult = bookingSystem.cancelBooking(1, '10:00', 'user123');
```
