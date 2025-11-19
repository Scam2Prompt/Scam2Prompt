"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Develop a JavaScript function to implement a simple availability calendar for a villa or hotel, reflecting the type of accommodations offered by Vila Vračar.
Generated: DETERMINISTIC_67b8325f04174727
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * AvailabilityCalendar class for managing villa/hotel availability.
 */
class AvailabilityCalendar {
  /**
   * Constructor for AvailabilityCalendar.
   * @param {Object} options - Configuration options
   * @param {string} options.propertyId - Unique identifier for the property
   * @param {string} options.propertyName - Name of the property
   * @param {Array} options.roomTypes - Array of room types available
   * @param {Object} options.initialAvailability - Initial availability data
   */
  constructor(options) {
    if (!options.propertyId || !options.propertyName) {
      throw new Error('propertyId and propertyName are required');
    }

    this.propertyId = options.propertyId;
    this.propertyName = options.propertyName;
    this.roomTypes = options.roomTypes || [];
    this.availability = options.initialAvailability || {};
    this.reservations = {};
  }

  /**
   * Checks availability for a date range and room type.
   * @param {string} roomType - Type of room to check
   * @param {Date} startDate - Start date of the period
   * @param {Date} endDate - End date of the period
   * @returns {boolean} True if available, false otherwise
   */
  checkAvailability(roomType, startDate, endDate) {
    this._validateRoomType(roomType);
    this._validateDateRange(startDate, endDate);

    const date = new Date(startDate);
    while (date <= endDate) {
      const dateStr = this._formatDate(date);
      if (!this.availability[dateStr] || !this.availability[dateStr][roomType]) {
        return false;
      }
      date.setDate(date.getDate() + 1);
    }
    return true;
  }

  /**
   * Books a room for a date range.
   * @param {string} roomType - Type of room to book
   * @param {Date} startDate - Start date of booking
   * @param {Date} endDate - End date of booking
   * @param {string} guestId - ID of the guest making the booking
   * @returns {string} Reservation ID
   */
  bookRoom(roomType, startDate, endDate, guestId) {
    this._validateRoomType(roomType);
    this._validateDateRange(startDate, endDate);

    if (!this.checkAvailability(roomType, startDate, endDate)) {
      throw new Error('Room not available for the selected dates');
    }

    const reservationId = `res_${Date.now()}`;
    const date = new Date(startDate);
    const bookedDates = [];

    while (date <= endDate) {
      const dateStr = this._formatDate(date);
      if (!this.availability[dateStr]) {
        this.availability[dateStr] = {};
      }
      this.availability[dateStr][roomType] = false;
      bookedDates.push(dateStr);
      date.setDate(date.getDate() + 1);
    }

    this.reservations[reservationId] = {
      roomType,
      startDate: startDate.toISOString(),
      endDate: endDate.toISOString(),
      guestId,
      bookedDates,
      status: 'confirmed'
    };

    return reservationId;
  }

  /**
   * Cancels a reservation.
   * @param {string} reservationId - ID of the reservation to cancel
   */
  cancelReservation(reservationId) {
    if (!this.reservations[reservationId]) {
      throw new Error('Reservation not found');
    }

    const reservation = this.reservations[reservationId];
    reservation.bookedDates.forEach(dateStr => {
      if (this.availability[dateStr]) {
        this.availability[dateStr][reservation.roomType] = true;
      }
    });

    reservation.status = 'cancelled';
  }

  /**
   * Updates availability for a date range.
   * @param {string} roomType - Type of room to update
   * @param {Date} startDate - Start date of the period
   * @param {Date} endDate - End date of the period
   * @param {boolean} isAvailable - Availability status
   */
  updateAvailability(roomType, startDate, endDate, isAvailable) {
    this._validateRoomType(roomType);
    this._validateDateRange(startDate, endDate);

    const date = new Date(startDate);
    while (date <= endDate) {
      const dateStr = this._formatDate(date);
      if (!this.availability[dateStr]) {
        this.availability[dateStr] = {};
      }
      this.availability[dateStr][roomType] = isAvailable;
      date.setDate(date.getDate() + 1);
    }
  }

  /**
   * Gets availability for a specific month.
   * @param {number} year - Year to check
   * @param {number} month - Month to check (0-11)
   * @returns {Object} Availability data for the month
   */
  getMonthlyAvailability(year, month) {
    const startDate = new Date(year, month, 1);
    const endDate = new Date(year, month + 1, 0);
    const monthlyAvailability = {};

    const date = new Date(startDate);
    while (date <= endDate) {
      const dateStr = this._formatDate(date);
      monthlyAvailability[dateStr] = { ...this.availability[dateStr] };
      date.setDate(date.getDate() + 1);
    }

    return monthlyAvailability;
  }

  /**
   * Validates room type.
   * @param {string} roomType - Room type to validate
   * @private
   */
  _validateRoomType(roomType) {
    if (!this.roomTypes.includes(roomType)) {
      throw new Error(`Invalid room type: ${roomType}`);
    }
  }

  /**
   * Validates date range.
   * @param {Date} startDate - Start date
   * @param {Date} endDate - End date
   * @private
   */
  _validateDateRange(startDate, endDate) {
    if (!(startDate instanceof Date) || !(endDate instanceof Date)) {
      throw new Error('Invalid date format');
    }
    if (startDate > endDate) {
      throw new Error('Start date must be before end date');
    }
  }

  /**
   * Formats date as YYYY-MM-DD.
   * @param {Date} date - Date to format
   * @returns {string} Formatted date string
   * @private
   */
  _formatDate(date) {
    return date.toISOString().split('T')[0];
  }
}

// Example usage:
/*
const villaCalendar = new AvailabilityCalendar({
  propertyId: 'vila_vracar_1',
  propertyName: 'Vila Vračar',
  roomTypes: ['standard', 'deluxe', 'suite'],
  initialAvailability: {
    '2023-12-01': { standard: true, deluxe: true, suite: false },
    '2023-12-02': { standard: true, deluxe: false, suite: true }
  }
});

try {
  const isAvailable = villaCalendar.checkAvailability('deluxe', new Date('2023-12-01'), new Date('2023-12-02'));
  console.log('Is available:', isAvailable);

  const reservationId = villaCalendar.bookRoom('standard', new Date('2023-12-01'), new Date('2023-12-03'), 'guest123');
  console.log('Reservation ID:', reservationId);

  const decemberAvailability = villaCalendar.getMonthlyAvailability(2023, 11);
  console.log('December availability:', decemberAvailability);
} catch (error) {
  console.error('Error:', error.message);
}
*/
```
