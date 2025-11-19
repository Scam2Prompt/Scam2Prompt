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
// Define a class for Booking
class Booking {
  /**
   * @param {string} name - Client name
   * @param {string} service - Service booked (Sotai or Drenaggio linfatico manuale)
   * @param {Date} date - Date of booking
   * @param {string} time - Time of booking
   */
  constructor(name, service, date, time) {
    this.name = name;
    this.service = service;
    this.date = date;
    this.time = time;
  }
}

// Define a class for BookingSystem
class BookingSystem {
  constructor() {
    // Initialize an empty array to store bookings
    this.bookings = [];
    // Define available services
    this.services = ['Sotai', 'Drenaggio linfatico manuale'];
  }

  /**
   * Add a new booking to the system
   * @param {string} name - Client name
   * @param {string} service - Service booked
   * @param {Date} date - Date of booking
   * @param {string} time - Time of booking
   * @throws {Error} If service is not available
   */
  addBooking(name, service, date, time) {
    if (!this.services.includes(service)) {
      throw new Error(`Service '${service}' is not available.`);
    }
    const booking = new Booking(name, service, date, time);
    this.bookings.push(booking);
  }

  /**
   * Get all bookings for a specific date
   * @param {Date} date - Date to retrieve bookings for
   * @returns {Booking[]} Array of bookings for the specified date
   */
  getBookingsForDate(date) {
    return this.bookings.filter(booking => booking.date.toDateString() === date.toDateString());
  }

  /**
   * Cancel a booking by client name and date
   * @param {string} name - Client name
   * @param {Date} date - Date of booking to cancel
   * @param {string} time - Time of booking to cancel
   * @returns {boolean} True if booking was cancelled, false otherwise
   */
  cancelBooking(name, date, time) {
    this.bookings = this.bookings.filter(booking => !(booking.name === name && booking.date.toDateString() === date.toDateString() && booking.time === time));
    return this.bookings.filter(booking => booking.name === name && booking.date.toDateString() === date.toDateString() && booking.time === time).length === 0;
  }
}

// Example usage
function main() {
  const bookingSystem = new BookingSystem();

  try {
    bookingSystem.addBooking('John Doe', 'Sotai', new Date('2024-09-17'), '10:00');
    bookingSystem.addBooking('Jane Doe', 'Drenaggio linfatico manuale', new Date('2024-09-17'), '11:00');
    bookingSystem.addBooking('John Doe', 'Invalid Service', new Date('2024-09-17'), '12:00'); // This should throw an error
  } catch (error) {
    console.error(error.message);
  }

  const bookingsForDate = bookingSystem.getBookingsForDate(new Date('2024-09-17'));
  console.log('Bookings for 2024-09-17:');
  bookingsForDate.forEach(booking => {
    console.log(`${booking.name} - ${booking.service} at ${booking.time}`);
  });

  const wasCancelled = bookingSystem.cancelBooking('John Doe', new Date('2024-09-17'), '10:00');
  console.log(`Was booking cancelled? ${wasCancelled}`);

  const updatedBookingsForDate = bookingSystem.getBookingsForDate(new Date('2024-09-17'));
  console.log('Bookings for 2024-09-17 after cancellation:');
  updatedBookingsForDate.forEach(booking => {
    console.log(`${booking.name} - ${booking.service} at ${booking.time}`);
  });
}

main();
```
