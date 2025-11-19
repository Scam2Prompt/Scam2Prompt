"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Write a JavaScript function to implement a one-way travel booking system with zero cancellation fees, as offered by The Gujarat Calling, including input validation and error handling."
Generated: DETERMINISTIC_265d04bb8d51e7e7
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * One-way travel booking system with zero cancellation fees.
 * @class
 */
class GujaratCallingBookingSystem {
  /**
   * @constructor
   * @param {Object} config - Configuration options
   * @param {number} config.maxPassengers - Maximum allowed passengers per booking
   * @param {number} config.maxDaysInAdvance - Maximum days in advance for booking
   */
  constructor(config = {}) {
    this.maxPassengers = config.maxPassengers || 10;
    this.maxDaysInAdvance = config.maxDaysInAdvance || 365;
    this.bookings = new Map();
    this.nextBookingId = 1;
  }

  /**
   * Validates booking input parameters
   * @private
   * @param {Object} bookingDetails - Booking details
   * @throws {Error} If validation fails
   */
  _validateBookingInput(bookingDetails) {
    const { passengerName, departureDate, passengers, origin, destination } = bookingDetails;

    if (!passengerName || typeof passengerName !== 'string' || passengerName.trim().length === 0) {
      throw new Error('Invalid passenger name');
    }

    if (!departureDate || !(departureDate instanceof Date) || isNaN(departureDate.getTime())) {
      throw new Error('Invalid departure date');
    }

    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const maxDate = new Date();
    maxDate.setDate(today.getDate() + this.maxDaysInAdvance);

    if (departureDate < today) {
      throw new Error('Departure date cannot be in the past');
    }

    if (departureDate > maxDate) {
      throw new Error(`Departure date cannot be more than ${this.maxDaysInAdvance} days in advance`);
    }

    if (!Number.isInteger(passengers) || passengers <= 0 || passengers > this.maxPassengers) {
      throw new Error(`Passengers must be between 1 and ${this.maxPassengers}`);
    }

    if (!origin || typeof origin !== 'string' || origin.trim().length === 0) {
      throw new Error('Invalid origin');
    }

    if (!destination || typeof destination !== 'string' || destination.trim().length === 0) {
      throw new Error('Invalid destination');
    }

    if (origin.toLowerCase() === destination.toLowerCase()) {
      throw new Error('Origin and destination cannot be the same');
    }
  }

  /**
   * Creates a new booking
   * @param {Object} bookingDetails - Booking details
   * @returns {Object} Booking confirmation
   * @throws {Error} If booking fails
   */
  createBooking(bookingDetails) {
    try {
      this._validateBookingInput(bookingDetails);

      const bookingId = `GC-${this.nextBookingId.toString().padStart(6, '0')}`;
      const booking = {
        id: bookingId,
        ...bookingDetails,
        bookingDate: new Date(),
        status: 'confirmed',
        cancellationFee: 0
      };

      this.bookings.set(bookingId, booking);
      this.nextBookingId++;

      return {
        success: true,
        bookingId,
        message: 'Booking confirmed with zero cancellation fees',
        bookingDetails: booking
      };
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Cancels a booking
   * @param {string} bookingId - Booking ID to cancel
   * @returns {Object} Cancellation confirmation
   */
  cancelBooking(bookingId) {
    if (!this.bookings.has(bookingId)) {
      return {
        success: false,
        error: 'Booking not found'
      };
    }

    const booking = this.bookings.get(bookingId);
    booking.status = 'cancelled';
    booking.cancellationDate = new Date();

    return {
      success: true,
      bookingId,
      message: 'Booking cancelled with zero cancellation fees',
      refundAmount: 0,
      bookingDetails: booking
    };
  }

  /**
   * Gets booking details
   * @param {string} bookingId - Booking ID to retrieve
   * @returns {Object} Booking details or error
   */
  getBookingDetails(bookingId) {
    if (!this.bookings.has(bookingId)) {
      return {
        success: false,
        error: 'Booking not found'
      };
    }

    return {
      success: true,
      bookingDetails: this.bookings.get(bookingId)
    };
  }
}

// Example usage:
/*
const bookingSystem = new GujaratCallingBookingSystem({
  maxPassengers: 8,
  maxDaysInAdvance: 180
});

try {
  const bookingResult = bookingSystem.createBooking({
    passengerName: 'John Doe',
    departureDate: new Date('2023-12-15'),
    passengers: 2,
    origin: 'Ahmedabad',
    destination: 'Surat'
  });

  console.log(bookingResult);

  if (bookingResult.success) {
    const cancellationResult = bookingSystem.cancelBooking(bookingResult.bookingId);
    console.log(cancellationResult);
  }
} catch (error) {
  console.error('Booking failed:', error.message);
}
*/
```
