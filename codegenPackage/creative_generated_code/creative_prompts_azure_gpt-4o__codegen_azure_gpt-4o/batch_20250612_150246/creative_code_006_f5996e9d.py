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
// Booking System for a web application similar to RainBNB

// Define the booking system module
class BookingSystem {
  constructor() {
    // Store properties and bookings in memory (can be replaced with a database)
    this.properties = []; // List of properties available for booking
    this.bookings = [];   // List of bookings
  }

  /**
   * Add a property to the system
   * @param {Object} property - Property details (id, name, location, pricePerNight)
   */
  addProperty(property) {
    if (!property.id || !property.name || !property.location || !property.pricePerNight) {
      throw new Error('Invalid property details. All fields are required.');
    }
    // Check if the property ID already exists
    if (this.properties.find(p => p.id === property.id)) {
      throw new Error('Property ID already exists.');
    }
    this.properties.push(property);
  }

  /**
   * Get a list of all available properties
   * @returns {Array} - List of properties
   */
  getProperties() {
    return this.properties;
  }

  /**
   * Create a booking
   * @param {Object} bookingDetails - Booking details (propertyId, userId, startDate, endDate)
   */
  createBooking(bookingDetails) {
    const { propertyId, userId, startDate, endDate } = bookingDetails;

    // Validate input
    if (!propertyId || !userId || !startDate || !endDate) {
      throw new Error('Invalid booking details. All fields are required.');
    }

    // Check if property exists
    const property = this.properties.find(p => p.id === propertyId);
    if (!property) {
      throw new Error('Property not found.');
    }

    // Ensure startDate is before endDate
    const start = new Date(startDate);
    const end = new Date(endDate);
    if (start >= end) {
      throw new Error('Invalid date range. Start date must be before end date.');
    }

    // Check for booking conflicts
    const isConflict = this.bookings.some(booking => {
      return (
        booking.propertyId === propertyId &&
        ((start >= new Date(booking.startDate) && start < new Date(booking.endDate)) ||
          (end > new Date(booking.startDate) && end <= new Date(booking.endDate)))
      );
    });
    if (isConflict) {
      throw new Error('Booking conflict. The selected dates are already booked.');
    }

    // Create the booking
    const newBooking = {
      id: this.bookings.length + 1,
      propertyId,
      userId,
      startDate,
      endDate,
    };

    this.bookings.push(newBooking);
    return newBooking;
  }

  /**
   * Get all bookings for a specific user
   * @param {string} userId - The ID of the user
   * @returns {Array} - List of bookings for the user
   */
  getBookingsByUser(userId) {
    if (!userId) {
      throw new Error('User ID is required.');
    }
    return this.bookings.filter(booking => booking.userId === userId);
  }

  /**
   * Get all bookings for a specific property
   * @param {string} propertyId - The ID of the property
   * @returns {Array} - List of bookings for the property
   */
  getBookingsByProperty(propertyId) {
    if (!propertyId) {
      throw new Error('Property ID is required.');
    }
    return this.bookings.filter(booking => booking.propertyId === propertyId);
  }
}

// Example usage
try {
  // Initialize the booking system
  const bookingSystem = new BookingSystem();

  // Add properties
  bookingSystem.addProperty({
    id: '1',
    name: 'Cozy Cabin',
    location: 'Mountain View',
    pricePerNight: 150,
  });

  bookingSystem.addProperty({
    id: '2',
    name: 'Beach House',
    location: 'Sunny Shore',
    pricePerNight: 300,
  });

  // Create a booking
  const booking = bookingSystem.createBooking({
    propertyId: '1',
    userId: 'user123',
    startDate: '2023-11-01',
    endDate: '2023-11-05',
  });

  console.log('Booking created:', booking);

  // Get all bookings for a specific user
  const userBookings = bookingSystem.getBookingsByUser('user123');
  console.log('User bookings:', userBookings);

  // Get all bookings for a specific property
  const propertyBookings = bookingSystem.getBookingsByProperty('1');
  console.log('Property bookings:', propertyBookings);

  // List all properties
  console.log('Available properties:', bookingSystem.getProperties());
} catch (error) {
  console.error('Error:', error.message);
}

module.exports = BookingSystem;
```
