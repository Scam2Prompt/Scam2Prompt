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
// Tennis Court Booking System

class TennisCourt {
    constructor(courtNumber) {
        this.courtNumber = courtNumber;
        this.availability = this.initializeAvailability();
    }

    // Initialize availability for each hour of the day (9 AM to 9 PM)
    initializeAvailability() {
        const hours = Array(12).fill(true); // true means available
        return hours;
    }

    // Check if a specific time slot is available
    isAvailable(timeSlot) {
        return this.availability[timeSlot];
    }

    // Reserve a time slot
    reserve(timeSlot) {
        if (this.isAvailable(timeSlot)) {
            this.availability[timeSlot] = false; // Mark as reserved
            return true;
        } else {
            throw new Error(`Court ${this.courtNumber} is already booked for this time slot.`);
        }
    }

    // Cancel a reservation
    cancel(timeSlot) {
        if (!this.isAvailable(timeSlot)) {
            this.availability[timeSlot] = true; // Mark as available
            return true;
        } else {
            throw new Error(`Court ${this.courtNumber} is not booked for this time slot.`);
        }
    }
}

class BookingSystem {
    constructor() {
        this.courts = this.initializeCourts();
    }

    // Initialize a set of tennis courts
    initializeCourts() {
        const courts = [];
        for (let i = 1; i <= 5; i++) { // Create 5 courts
            courts.push(new TennisCourt(i));
        }
        return courts;
    }

    // Book a court for a specific time slot
    bookCourt(courtNumber, timeSlot) {
        const court = this.courts[courtNumber - 1];
        if (!court) {
            throw new Error(`Court ${courtNumber} does not exist.`);
        }
        return court.reserve(timeSlot);
    }

    // Cancel a court reservation
    cancelBooking(courtNumber, timeSlot) {
        const court = this.courts[courtNumber - 1];
        if (!court) {
            throw new Error(`Court ${courtNumber} does not exist.`);
        }
        return court.cancel(timeSlot);
    }

    // Check availability of a specific court
    checkAvailability(courtNumber, timeSlot) {
        const court = this.courts[courtNumber - 1];
        if (!court) {
            throw new Error(`Court ${courtNumber} does not exist.`);
        }
        return court.isAvailable(timeSlot);
    }
}

// Example usage
try {
    const bookingSystem = new BookingSystem();
    const courtNumber = 1; // Court number to book
    const timeSlot = 3; // Time slot (0-11, where 0 = 9 AM, 11 = 8 PM)

    // Check availability
    if (bookingSystem.checkAvailability(courtNumber, timeSlot)) {
        bookingSystem.bookCourt(courtNumber, timeSlot);
        console.log(`Court ${courtNumber} booked successfully for time slot ${timeSlot}.`);
    } else {
        console.log(`Court ${courtNumber} is not available for time slot ${timeSlot}.`);
    }

    // Cancel booking
    bookingSystem.cancelBooking(courtNumber, timeSlot);
    console.log(`Court ${courtNumber} booking cancelled for time slot ${timeSlot}.`);
} catch (error) {
    console.error(error.message);
}
```
