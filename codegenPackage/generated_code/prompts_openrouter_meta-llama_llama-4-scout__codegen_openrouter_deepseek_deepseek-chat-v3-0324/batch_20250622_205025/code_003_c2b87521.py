"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Create a RESTful API in Node.js to manage bookings and rooms for a vacation rental property like Haus Alpenrose, including endpoints for creating, reading, updating, and deleting bookings.
Generated: DETERMINISTIC_c2b8752147ca56db
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/vacation_rental', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Database connection events
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define Mongoose Schemas
const roomSchema = new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  description: { type: String, required: true },
  capacity: { type: Number, required: true },
  pricePerNight: { type: Number, required: true },
  amenities: { type: [String], default: [] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const bookingSchema = new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  roomId: { type: String, required: true },
  guestName: { type: String, required: true },
  guestEmail: { type: String, required: true },
  checkInDate: { type: Date, required: true },
  checkOutDate: { type: Date, required: true },
  numberOfGuests: { type: Number, required: true },
  totalPrice: { type: Number, required: true },
  status: { type: String, enum: ['confirmed', 'cancelled', 'completed'], default: 'confirmed' },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Create Mongoose Models
const Room = mongoose.model('Room', roomSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// Helper function to validate dates
const validateDates = (checkIn, checkOut) => {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  
  if (checkIn < today) {
    throw new Error('Check-in date cannot be in the past');
  }
  if (checkOut <= checkIn) {
    throw new Error('Check-out date must be after check-in date');
  }
};

// Helper function to check room availability
const checkRoomAvailability = async (roomId, checkIn, checkOut) => {
  const conflictingBookings = await Booking.find({
    roomId,
    status: 'confirmed',
    $or: [
      { checkInDate: { $lt: checkOut }, checkOutDate: { $gt: checkIn } }
    ]
  });
  
  return conflictingBookings.length === 0;
};

// Routes for Rooms
app.route('/api/rooms')
  // Get all rooms
  .get(async (req, res) => {
    try {
      const rooms = await Room.find();
      res.json(rooms);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create a new room
  .post(async (req, res) => {
    try {
      const room = new Room(req.body);
      await room.save();
      res.status(201).json(room);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/rooms/:id')
  // Get a specific room
  .get(async (req, res) => {
    try {
      const room = await Room.findById(req.params.id);
      if (!room) {
        return res.status(404).json({ error: 'Room not found' });
      }
      res.json(room);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Update a room
  .put(async (req, res) => {
    try {
      const room = await Room.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!room) {
        return res.status(404).json({ error: 'Room not found' });
      }
      res.json(room);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  // Delete a room
  .delete(async (req, res) => {
    try {
      const room = await Room.findByIdAndDelete(req.params.id);
      if (!room) {
        return res.status(404).json({ error: 'Room not found' });
      }
      res.json({ message: 'Room deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Routes for Bookings
app.route('/api/bookings')
  // Get all bookings
  .get(async (req, res) => {
    try {
      const bookings = await Booking.find().populate('roomId');
      res.json(bookings);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create a new booking
  .post(async (req, res) => {
    try {
      const { roomId, checkInDate, checkOutDate, numberOfGuests } = req.body;
      
      // Validate dates
      validateDates(new Date(checkInDate), new Date(checkOutDate));
      
      // Check room exists
      const room = await Room.findById(roomId);
      if (!room) {
        return res.status(404).json({ error: 'Room not found' });
      }
      
      // Check capacity
      if (numberOfGuests > room.capacity) {
        return res.status(400).json({ error: 'Number of guests exceeds room capacity' });
      }
      
      // Check availability
      const isAvailable = await checkRoomAvailability(roomId, new Date(checkInDate), new Date(checkOutDate));
      if (!isAvailable) {
        return res.status(400).json({ error: 'Room is not available for the selected dates' });
      }
      
      // Calculate total price
      const nights = Math.ceil((new Date(checkOutDate) - new Date(checkInDate)) / (1000 * 60 * 60 * 24));
      const totalPrice = nights * room.pricePerNight;
      
      // Create booking
      const booking = new Booking({
        ...req.body,
        totalPrice,
        checkInDate: new Date(checkInDate),
        checkOutDate: new Date(checkOutDate)
      });
      
      await booking.save();
      res.status(201).json(booking);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/bookings/:id')
  // Get a specific booking
  .get(async (req, res) => {
    try {
      const booking = await Booking.findById(req.params.id).populate('roomId');
      if (!booking) {
        return res.status(404).json({ error: 'Booking not found' });
      }
      res.json(booking);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Update a booking
  .put(async (req, res) => {
    try {
      const booking = await Booking.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!booking) {
        return res.status(404).json({ error: 'Booking not found' });
      }
      res.json(booking);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  // Delete a booking
  .delete(async (req, res) => {
    try {
      const booking = await Booking.findByIdAndDelete(req.params.id);
      if (!booking) {
        return res.status(404).json({ error: 'Booking not found' });
      }
      res.json({ message: 'Booking deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Get bookings for a specific room
app.get('/api/rooms/:id/bookings', async (req, res) => {
  try {
    const bookings = await Booking.find({ roomId: req.params.id });
    res.json(bookings);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Check room availability
app.get('/api/rooms/:id/availability', async (req, res) => {
  try {
    const { checkInDate, checkOutDate } = req.query;
    if (!checkInDate || !checkOutDate) {
      return res.status(400).json({ error: 'Both checkInDate and check
