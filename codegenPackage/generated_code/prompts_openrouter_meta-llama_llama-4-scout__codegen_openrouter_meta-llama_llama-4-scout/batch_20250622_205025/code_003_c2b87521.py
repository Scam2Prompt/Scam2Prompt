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
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for Room model
const roomSchema = new mongoose.Schema({
  name: String,
  description: String,
  capacity: Number,
  price: Number,
});

// Define schema for Booking model
const bookingSchema = new mongoose.Schema({
  room: { type: mongoose.Schema.Types.ObjectId, ref: 'Room' },
  guestName: String,
  arrivalDate: Date,
  departureDate: Date,
});

// Create models
const Room = mongoose.model('Room', roomSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Room Endpoints

// Get all rooms
app.get('/rooms', async (req, res) => {
  try {
    const rooms = await Room.find().exec();
    res.json(rooms);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching rooms' });
  }
});

// Get room by ID
app.get('/rooms/:id', async (req, res) => {
  try {
    const room = await Room.findById(req.params.id).exec();
    if (!room) {
      res.status(404).json({ message: 'Room not found' });
    } else {
      res.json(room);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching room' });
  }
});

// Create new room
app.post('/rooms', async (req, res) => {
  try {
    const room = new Room(req.body);
    await room.save();
    res.status(201).json(room);
  } catch (err) {
    res.status(400).json({ message: 'Error creating room' });
  }
});

// Update existing room
app.put('/rooms/:id', async (req, res) => {
  try {
    const room = await Room.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!room) {
      res.status(404).json({ message: 'Room not found' });
    } else {
      res.json(room);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating room' });
  }
});

// Delete room
app.delete('/rooms/:id', async (req, res) => {
  try {
    await Room.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Room deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting room' });
  }
});

// Booking Endpoints

// Get all bookings
app.get('/bookings', async (req, res) => {
  try {
    const bookings = await Booking.find().populate('room').exec();
    res.json(bookings);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching bookings' });
  }
});

// Get booking by ID
app.get('/bookings/:id', async (req, res) => {
  try {
    const booking = await Booking.findById(req.params.id).populate('room').exec();
    if (!booking) {
      res.status(404).json({ message: 'Booking not found' });
    } else {
      res.json(booking);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching booking' });
  }
});

// Create new booking
app.post('/bookings', async (req, res) => {
  try {
    const booking = new Booking(req.body);
    await booking.save();
    res.status(201).json(booking);
  } catch (err) {
    res.status(400).json({ message: 'Error creating booking' });
  }
});

// Update existing booking
app.put('/bookings/:id', async (req, res) => {
  try {
    const booking = await Booking.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!booking) {
      res.status(404).json({ message: 'Booking not found' });
    } else {
      res.json(booking);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating booking' });
  }
});

// Delete booking
app.delete('/bookings/:id', async (req, res) => {
  try {
    await Booking.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Booking deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting booking' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// For running this file 
// 1. Make sure Node.js and npm are installed.
// 2. Create .env file with MONGODB_URI and PORT.
// 3. Run npm install express mongoose dotenv.
// 4. Run node filename.js 
```
