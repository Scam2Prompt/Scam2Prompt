"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rainbnb.live
Prompt: Write code to implement a JavaScript-based booking system for a web application, similar to what RainBNB might offer.
Generated: DETERMINISTIC_f5996e9dc0e8b413
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// bookingSystem.js

class BookingSystem {
    constructor() {
        // Initialize an empty array to hold bookings
        this.bookings = [];
    }

    /**
     * Method to add a new booking
     * @param {Object} booking - The booking object containing details of the booking
     * @param {string} booking.name - The name of the person making the booking
     * @param {string} booking.propertyId - The ID of the property being booked
     * @param {Date} booking.startDate - The start date of the booking
     * @param {Date} booking.endDate - The end date of the booking
     * @throws Will throw an error if the booking dates are invalid or if the property is already booked
     */
    addBooking(booking) {
        this.validateBooking(booking);
        this.bookings.push(booking);
    }

    /**
     * Method to validate booking details
     * @param {Object} booking - The booking object to validate
     * @throws Will throw an error if the booking is invalid
     */
    validateBooking(booking) {
        const { name, propertyId, startDate, endDate } = booking;

        // Check if required fields are present
        if (!name || !propertyId || !startDate || !endDate) {
            throw new Error('All booking fields must be provided.');
        }

        // Validate date range
        const start = new Date(startDate);
        const end = new Date(endDate);
        if (isNaN(start) || isNaN(end) || start >= end) {
            throw new Error('Invalid booking date range.');
        }

        // Check for conflicting bookings
        const isBooked = this.bookings.some(b => 
            b.propertyId === propertyId &&
            ((start >= new Date(b.startDate) && start < new Date(b.endDate)) ||
            (end > new Date(b.startDate) && end <= new Date(b.endDate)))
        );

        if (isBooked) {
            throw new Error('The property is already booked for the selected dates.');
        }
    }

    /**
     * Method to retrieve all bookings
     * @returns {Array} - An array of all bookings
     */
    getBookings() {
        return this.bookings;
    }

    /**
     * Method to clear all bookings (for testing purposes)
     */
    clearBookings() {
        this.bookings = [];
    }
}

// Usage Example
try {
    const bookingSystem = new BookingSystem();

    // Sample booking
    const booking1 = {
        name: "John Doe",
        propertyId: "prop123",
        startDate: "2023-11-01",
        endDate: "2023-11-10",
    };

    bookingSystem.addBooking(booking1);
    console.log('Booking added successfully:', bookingSystem.getBookings());

    // Attempting to add a conflicting booking
    const booking2 = {
        name: "Jane Smith",
        propertyId: "prop123",
        startDate: "2023-11-05",
        endDate: "2023-11-12",
    };

    bookingSystem.addBooking(booking2); // This should throw an error
} catch (error) {
    console.error('Error adding booking:', error.message);
}
```

This code implements a simple JavaScript-based booking system with error handling and validation. The `BookingSystem` class manages bookings, ensuring that bookings are valid and do not conflict with existing ones.
