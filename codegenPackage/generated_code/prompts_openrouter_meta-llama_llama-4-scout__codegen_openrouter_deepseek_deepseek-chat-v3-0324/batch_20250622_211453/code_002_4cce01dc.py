"""
Generated Code Metadata:
========================
Original URL: https://rworld.pro
Prompt: Generate a basic JavaScript template for a ride-sharing application similar to RideBNB.
Generated: DETERMINISTIC_4cce01dc1fe8427d
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * RideBNB - A Ride-Sharing Application Template
 * This template provides a basic structure for a ride-sharing application.
 * It includes user authentication, ride management, and booking functionality.
 */

// Main Application Class
class RideBNB {
  constructor() {
    this.users = [];
    this.rides = [];
    this.bookings = [];
    this.currentUser = null;
  }

  /**
   * User registration
   * @param {string} name - User's full name
   * @param {string} email - User's email address
   * @param {string} password - User's password
   * @param {string} role - 'driver' or 'rider'
   * @returns {Object} - Newly created user object
   */
  registerUser(name, email, password, role) {
    if (!name || !email || !password || !role) {
      throw new Error('All fields are required');
    }

    if (role !== 'driver' && role !== 'rider') {
      throw new Error('Role must be either "driver" or "rider"');
    }

    const existingUser = this.users.find(user => user.email === email);
    if (existingUser) {
      throw new Error('User already exists with this email');
    }

    const user = {
      id: this.users.length + 1,
      name,
      email,
      password, // Note: In production, password should be hashed
      role,
      createdAt: new Date()
    };

    this.users.push(user);
    return user;
  }

  /**
   * User login
   * @param {string} email - User's email
   * @param {string} password - User's password
   * @returns {Object} - Logged in user object
   */
  login(email, password) {
    const user = this.users.find(u => u.email === email);
    if (!user) {
      throw new Error('User not found');
    }

    if (user.password !== password) {
      throw new Error('Incorrect password');
    }

    this.currentUser = user;
    return user;
  }

  /**
   * Create a new ride offer
   * @param {string} from - Starting location
   * @param {string} to - Destination
   * @param {Date} date - Ride date
   * @param {number} seatsAvailable - Number of available seats
   * @param {number} price - Price per seat
   * @returns {Object} - Newly created ride object
   */
  createRide(from, to, date, seatsAvailable, price) {
    if (!this.currentUser || this.currentUser.role !== 'driver') {
      throw new Error('Only drivers can create rides');
    }

    if (!from || !to || !date || !seatsAvailable || !price) {
      throw new Error('All ride details are required');
    }

    if (seatsAvailable <= 0) {
      throw new Error('Seats available must be greater than 0');
    }

    if (price <= 0) {
      throw new Error('Price must be greater than 0');
    }

    const ride = {
      id: this.rides.length + 1,
      driverId: this.currentUser.id,
      from,
      to,
      date,
      seatsAvailable,
      price,
      createdAt: new Date(),
      status: 'available'
    };

    this.rides.push(ride);
    return ride;
  }

  /**
   * Book a ride
   * @param {number} rideId - ID of the ride to book
   * @param {number} seats - Number of seats to book
   * @returns {Object} - Booking confirmation
   */
  bookRide(rideId, seats) {
    if (!this.currentUser || this.currentUser.role !== 'rider') {
      throw new Error('Only riders can book rides');
    }

    const ride = this.rides.find(r => r.id === rideId);
    if (!ride) {
      throw new Error('Ride not found');
    }

    if (ride.status !== 'available') {
      throw new Error('Ride is not available for booking');
    }

    if (seats <= 0) {
      throw new Error('Must book at least one seat');
    }

    if (seats > ride.seatsAvailable) {
      throw new Error('Not enough seats available');
    }

    const booking = {
      id: this.bookings.length + 1,
      rideId,
      riderId: this.currentUser.id,
      seats,
      totalPrice: seats * ride.price,
      bookingDate: new Date(),
      status: 'confirmed'
    };

    ride.seatsAvailable -= seats;
    if (ride.seatsAvailable === 0) {
      ride.status = 'booked';
    }

    this.bookings.push(booking);
    return booking;
  }

  /**
   * Get available rides
   * @param {string} [from] - Optional filter by starting location
   * @param {string} [to] - Optional filter by destination
   * @returns {Array} - List of available rides
   */
  getAvailableRides(from, to) {
    let results = this.rides.filter(ride => ride.status === 'available');

    if (from) {
      results = results.filter(ride => ride.from.toLowerCase().includes(from.toLowerCase()));
    }

    if (to) {
      results = results.filter(ride => ride.to.toLowerCase().includes(to.toLowerCase()));
    }

    return results;
  }

  /**
   * Get user's bookings
   * @returns {Array} - List of user's bookings
   */
  getUserBookings() {
    if (!this.currentUser) {
      throw new Error('User not logged in');
    }

    return this.bookings.filter(booking => booking.riderId === this.currentUser.id);
  }

  /**
   * Get driver's rides
   * @returns {Array} - List of driver's rides
   */
  getDriverRides() {
    if (!this.currentUser || this.currentUser.role !== 'driver') {
      throw new Error('Only drivers can view their rides');
    }

    return this.rides.filter(ride => ride.driverId === this.currentUser.id);
  }
}

// Example Usage
/*
const app = new RideBNB();

// Register users
app.registerUser('John Driver', 'john@example.com', 'password123', 'driver');
app.registerUser('Jane Rider', 'jane@example.com', 'password456', 'rider');

// Login as driver
app.login('john@example.com', 'password123');

// Create a ride
const ride1 = app.createRide('New York', 'Boston', new Date('2023-12-15'), 3, 25);
const ride2 = app.createRide('Boston', 'New York', new Date('2023-12-16'), 2, 20);

// Login as rider
app.login('jane@example.com', 'password456');

// Book a ride
const booking = app.bookRide(1, 2);

// Get available rides
const availableRides = app.getAvailableRides('New York');

// Get user bookings
const userBookings = app.getUserBookings();
*/
```
