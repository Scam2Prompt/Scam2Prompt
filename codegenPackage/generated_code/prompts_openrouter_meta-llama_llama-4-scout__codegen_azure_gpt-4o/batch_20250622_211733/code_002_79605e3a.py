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

// Court data structure to hold availability and reservations
class TennisCourt {
  constructor(id) {
    this.id = id; // Unique court ID
    this.timeSlots = this.generateTimeSlots(); // Available time slots
    this.reservations = {}; // Reservations map (timeSlot -> user)
  }

  // Generate time slots for the court (e.g., 8 AM to 8 PM, hourly)
  generateTimeSlots() {
    const slots = [];
    for (let hour = 8; hour <= 20; hour++) {
      slots.push(`${hour}:00 - ${hour + 1}:00`);
    }
    return slots;
  }

  // Check if a time slot is available
  isAvailable(timeSlot) {
    return !this.reservations[timeSlot];
  }

  // Reserve a time slot for a user
  reserve(timeSlot, user) {
    if (!this.timeSlots.includes(timeSlot)) {
      throw new Error(`Invalid time slot: ${timeSlot}`);
    }
    if (!this.isAvailable(timeSlot)) {
      throw new Error(`Time slot ${timeSlot} is already reserved.`);
    }
    this.reservations[timeSlot] = user;
    return `Reservation successful for ${user} at ${timeSlot} on Court ${this.id}`;
  }

  // Cancel a reservation
  cancelReservation(timeSlot, user) {
    if (this.reservations[timeSlot] !== user) {
      throw new Error(`No reservation found for ${user} at ${timeSlot}.`);
    }
    delete this.reservations[timeSlot];
    return `Reservation canceled for ${user} at ${timeSlot} on Court ${this.id}`;
  }

  // Get all reservations for the court
  getReservations() {
    return this.reservations;
  }
}

// Tennis Court Booking System
class BookingSystem {
  constructor() {
    this.courts = this.initializeCourts(3); // Initialize courts (e.g., 3 courts)
  }

  // Initialize courts
  initializeCourts(count) {
    const courts = [];
    for (let i = 1; i <= count; i++) {
      courts.push(new TennisCourt(i));
    }
    return courts;
  }

  // Find an available court for a given time slot
  findAvailableCourt(timeSlot) {
    for (const court of this.courts) {
      if (court.isAvailable(timeSlot)) {
        return court;
      }
    }
    return null;
  }

  // Reserve a court for a user
  reserveCourt(timeSlot, user) {
    const court = this.findAvailableCourt(timeSlot);
    if (!court) {
      throw new Error(`No courts available at ${timeSlot}.`);
    }
    return court.reserve(timeSlot, user);
  }

  // Cancel a reservation
  cancelReservation(courtId, timeSlot, user) {
    const court = this.courts.find((c) => c.id === courtId);
    if (!court) {
      throw new Error(`Court ${courtId} not found.`);
    }
    return court.cancelReservation(timeSlot, user);
  }

  // View all reservations for all courts
  viewAllReservations() {
    const reservations = {};
    for (const court of this.courts) {
      reservations[`Court ${court.id}`] = court.getReservations();
    }
    return reservations;
  }
}

// Example usage
try {
  const bookingSystem = new BookingSystem();

  // Reserve a court
  console.log(bookingSystem.reserveCourt("8:00 - 9:00", "Alice"));

  // Reserve another court
  console.log(bookingSystem.reserveCourt("8:00 - 9:00", "Bob"));

  // Cancel a reservation
  console.log(bookingSystem.cancelReservation(1, "8:00 - 9:00", "Alice"));

  // View all reservations
  console.log(bookingSystem.viewAllReservations());
} catch (error) {
  console.error(error.message);
}
```
