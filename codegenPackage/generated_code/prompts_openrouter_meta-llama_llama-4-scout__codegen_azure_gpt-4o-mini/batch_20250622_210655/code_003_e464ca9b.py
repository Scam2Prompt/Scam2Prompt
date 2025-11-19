"""
Generated Code Metadata:
========================
Original URL: https://www.albertozofrea.it
Prompt: Write a code snippet in JavaScript to create a simple online booking system for a bodywork practice, including Sotai and Drenaggio linfatico manuale services.
Generated: DETERMINISTIC_e464ca9bfbac0383
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Booking System for Bodywork Practice

// Service class to represent a bodywork service
class Service {
    constructor(name, duration, price) {
        this.name = name; // Name of the service
        this.duration = duration; // Duration in minutes
        this.price = price; // Price of the service
    }
}

// Booking class to represent a booking
class Booking {
    constructor(clientName, service, dateTime) {
        this.clientName = clientName; // Name of the client
        this.service = service; // Service booked
        this.dateTime = dateTime; // Date and time of the booking
    }
}

// BookingSystem class to manage bookings
class BookingSystem {
    constructor() {
        this.services = []; // Array to hold available services
        this.bookings = []; // Array to hold bookings
    }

    // Method to add a service
    addService(service) {
        this.services.push(service);
    }

    // Method to create a booking
    createBooking(clientName, serviceName, dateTime) {
        // Validate inputs
        if (!clientName || !serviceName || !dateTime) {
            throw new Error("All fields are required to create a booking.");
        }

        // Find the service by name
        const service = this.services.find(s => s.name === serviceName);
        if (!service) {
            throw new Error("Service not found.");
        }

        // Create a new booking
        const booking = new Booking(clientName, service, dateTime);
        this.bookings.push(booking);
        return booking; // Return the created booking
    }

    // Method to list all bookings
    listBookings() {
        return this.bookings;
    }
}

// Initialize the booking system
const bookingSystem = new BookingSystem();

// Add services to the booking system
bookingSystem.addService(new Service("Sotai", 60, 70));
bookingSystem.addService(new Service("Drenaggio linfatico manuale", 90, 90));

// Example usage
try {
    const booking1 = bookingSystem.createBooking("John Doe", "Sotai", new Date("2023-10-15T10:00:00"));
    console.log("Booking created:", booking1);
    
    const booking2 = bookingSystem.createBooking("Jane Smith", "Drenaggio linfatico manuale", new Date("2023-10-16T14:00:00"));
    console.log("Booking created:", booking2);
    
    // List all bookings
    console.log("All bookings:", bookingSystem.listBookings());
} catch (error) {
    console.error("Error creating booking:", error.message);
}
```
