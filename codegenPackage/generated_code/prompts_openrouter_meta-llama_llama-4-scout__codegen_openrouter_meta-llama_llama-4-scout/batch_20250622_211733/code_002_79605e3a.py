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
// tennis-court-booking-system.js

class TennisCourt {
  /**
   * Represents a tennis court with its availability and reservations.
   * @param {string} name - The name of the tennis court.
   */
  constructor(name) {
    this.name = name;
    this.timeSlots = {};
    this.reservations = {};
  }

  /**
   * Initializes the tennis court's time slots.
   * @param {string[]} days - The days of the week (e.g., 'Monday', 'Tuesday', etc.).
   * @param {string[]} timeSlots - The time slots (e.g., '08:00-10:00', '10:00-12:00', etc.).
   */
  initTimeSlots(days, timeSlots) {
    days.forEach((day) => {
      this.timeSlots[day] = timeSlots;
    });
  }

  /**
   * Makes a reservation for a specific tennis court, day, and time slot.
   * @param {string} userName - The name of the user making the reservation.
   * @param {string} day - The day of the week.
   * @param {string} timeSlot - The time slot.
   * @returns {boolean} True if the reservation is successful, false otherwise.
   */
  makeReservation(userName, day, timeSlot) {
    if (!this.timeSlots[day] || !this.timeSlots[day].includes(timeSlot)) {
      throw new Error(`Invalid day or time slot: ${day} ${timeSlot}`);
    }

    if (this.reservations[`${day}_${timeSlot}`]) {
      return false; // Time slot already reserved
    }

    this.reservations[`${day}_${timeSlot}`] = userName;
    return true;
  }

  /**
   * Cancels a reservation for a specific tennis court, day, and time slot.
   * @param {string} day - The day of the week.
   * @param {string} timeSlot - The time slot.
   * @returns {boolean} True if the cancellation is successful, false otherwise.
   */
  cancelReservation(day, timeSlot) {
    if (!this.reservations[`${day}_${timeSlot}`]) {
      return false; // No reservation found
    }

    delete this.reservations[`${day}_${timeSlot}`];
    return true;
  }

  /**
   * Displays the tennis court's availability and reservations.
   */
  displayAvailability() {
    console.log(`Tennis Court: ${this.name}`);
    Object.keys(this.timeSlots).forEach((day) => {
      console.log(`  ${day}:`);
      this.timeSlots[day].forEach((timeSlot) => {
        const reserved = this.reservations[`${day}_${timeSlot}`] ? 'Reserved' : 'Available';
        console.log(`    ${timeSlot} - ${reserved}`);
      });
    });
  }
}

class TennisCourtBookingSystem {
  /**
   * Represents a tennis court booking system with multiple courts.
   */
  constructor() {
    this.courts = {};
  }

  /**
   * Adds a tennis court to the booking system.
   * @param {TennisCourt} court - The tennis court to add.
   */
  addCourt(court) {
    this.courts[court.name] = court;
  }

  /**
   * Displays the availability and reservations of all tennis courts.
   */
  displayCourtsAvailability() {
    Object.keys(this.courts).forEach((courtName) => {
      this.courts[courtName].displayAvailability();
      console.log(''); // Empty line for readability
    });
  }
}

// Example usage
function main() {
  try {
    const bookingSystem = new TennisCourtBookingSystem();

    const court1 = new TennisCourt('Court 1');
    court1.initTimeSlots(['Monday', 'Tuesday'], ['08:00-10:00', '10:00-12:00']);
    court1.makeReservation('John Doe', 'Monday', '08:00-10:00');

    const court2 = new TennisCourt('Court 2');
    court2.initTimeSlots(['Wednesday', 'Thursday'], ['14:00-16:00', '16:00-18:00']);
    court2.makeReservation('Jane Doe', 'Wednesday', '14:00-16:00');

    bookingSystem.addCourt(court1);
    bookingSystem.addCourt(court2);

    bookingSystem.displayCourtsAvailability();

    // Cancel a reservation
    court1.cancelReservation('Monday', '08:00-10:00');
    console.log('After cancellation:');
    bookingSystem.displayCourtsAvailability();
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
