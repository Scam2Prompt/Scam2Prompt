"""
Generated Code Metadata:
========================
Original URL: https://www.executivo2000.com
Prompt: Create a Node.js application to handle booking and management of lounge access for international, regional, and domestic flights, considering features like smoke-free areas and cocktail services.
Generated: DETERMINISTIC_2a1090e2b2b092ef
Batch ID: 20250622_210703
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
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect('mongodb://localhost:27017/loungeBooking', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('Database connection error:', err);
});

// Define Mongoose schemas
const loungeSchema = new mongoose.Schema({
  loungeId: { type: String, default: uuidv4, unique: true },
  name: { type: String, required: true },
  location: { type: String, required: true },
  type: { type: String, enum: ['international', 'regional', 'domestic'], required: true },
  smokeFree: { type: Boolean, default: false },
  cocktailService: { type: Boolean, default: false },
  capacity: { type: Number, required: true },
  amenities: { type: [String], default: [] },
  operatingHours: { type: String, required: true }
});

const bookingSchema = new mongoose.Schema({
  bookingId: { type: String, default: uuidv4, unique: true },
  loungeId: { type: String, required: true },
  passengerName: { type: String, required: true },
  flightNumber: { type: String, required: true },
  date: { type: Date, required: true },
  duration: { type: Number, required: true }, // in hours
  guests: { type: Number, default: 0 },
  specialRequests: { type: String, default: '' },
  createdAt: { type: Date, default: Date.now }
});

// Create models
const Lounge = mongoose.model('Lounge', loungeSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// API Routes

// Get all lounges
app.get('/api/lounges', async (req, res) => {
  try {
    const lounges = await Lounge.find();
    res.json(lounges);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch lounges' });
  }
});

// Get lounges by type
app.get('/api/lounges/:type', async (req, res) => {
  try {
    const { type } = req.params;
    const lounges = await Lounge.find({ type });
    res.json(lounges);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch lounges' });
  }
});

// Create a new booking
app.post('/api/bookings', async (req, res) => {
  try {
    const {
      loungeId,
      passengerName,
      flightNumber,
      date,
      duration,
      guests,
      specialRequests
    } = req.body;

    // Validate required fields
    if (!loungeId || !passengerName || !flightNumber || !date || !duration) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Check lounge availability (simplified)
    const lounge = await Lounge.findById(loungeId);
    if (!lounge) {
      return res.status(404).json({ error: 'Lounge not found' });
    }

    const booking = new Booking({
      loungeId,
      passengerName,
      flightNumber,
      date: new Date(date),
      duration,
      guests,
      specialRequests
    });

    await booking.save();
    res.status(201).json(booking);
  } catch (err) {
    res.status(500).json({ error: 'Failed to create booking' });
  }
});

// Get all bookings
app.get('/api/bookings', async (req, res) => {
  try {
    const bookings = await Booking.find().populate('loungeId');
    res.json(bookings);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch bookings' });
  }
});

// Get booking by ID
app.get('/api/bookings/:id', async (req, res) => {
  try {
    const booking = await Booking.findById(req.params.id).populate('loungeId');
    if (!booking) {
      return res.status(404).json({ error: 'Booking not found' });
    }
    res.json(booking);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch booking' });
  }
});

// Cancel booking
app.delete('/api/bookings/:id', async (req, res) => {
  try {
    const booking = await Booking.findByIdAndDelete(req.params.id);
    if (!booking) {
      return res.status(404).json({ error: 'Booking not found' });
    }
    res.json({ message: 'Booking cancelled successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to cancel booking' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
