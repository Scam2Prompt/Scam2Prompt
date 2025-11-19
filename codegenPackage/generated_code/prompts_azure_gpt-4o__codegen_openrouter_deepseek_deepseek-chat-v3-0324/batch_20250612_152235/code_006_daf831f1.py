"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Develop a Node.js application for managing event logistics, including attendee tracking, venue setup, and equipment rentals, based on the operational challenges faced by event companies.
Generated: DETERMINISTIC_daf831f1d6711f3f
Batch ID: 20250612_152235
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const { validationResult } = require('express-validator');
const { check } = require('express-validator');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect('mongodb://localhost:27017/eventManagement', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const Attendee = mongoose.model('Attendee', new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String },
  eventId: { type: mongoose.Schema.Types.ObjectId, ref: 'Event', required: true },
  checkInStatus: { type: Boolean, default: false },
  createdAt: { type: Date, default: Date.now }
}));

const Venue = mongoose.model('Venue', new mongoose.Schema({
  name: { type: String, required: true },
  capacity: { type: Number, required: true },
  location: { type: String, required: true },
  facilities: { type: [String], default: [] },
  bookedDates: { type: [Date], default: [] }
}));

const Equipment = mongoose.model('Equipment', new mongoose.Schema({
  name: { type: String, required: true },
  type: { type: String, required: true },
  quantity: { type: Number, required: true },
  rentalPrice: { type: Number, required: true },
  bookedDates: { type: [Date], default: [] }
}));

const Event = mongoose.model('Event', new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String },
  date: { type: Date, required: true },
  venueId: { type: mongoose.Schema.Types.ObjectId, ref: 'Venue', required: true },
  organizer: { type: String, required: true },
  equipmentIds: { type: [mongoose.Schema.Types.ObjectId], ref: 'Equipment', default: [] },
  status: { type: String, enum: ['planned', 'ongoing', 'completed'], default: 'planned' }
}));

// Validation middleware
const validateAttendee = [
  check('name').not().isEmpty().withMessage('Name is required'),
  check('email').isEmail().withMessage('Valid email is required'),
  check('eventId').not().isEmpty().withMessage('Event ID is required')
];

const validateVenue = [
  check('name').not().isEmpty().withMessage('Venue name is required'),
  check('capacity').isInt({ min: 1 }).withMessage('Capacity must be at least 1'),
  check('location').not().isEmpty().withMessage('Location is required')
];

const validateEquipment = [
  check('name').not().isEmpty().withMessage('Equipment name is required'),
  check('type').not().isEmpty().withMessage('Equipment type is required'),
  check('quantity').isInt({ min: 1 }).withMessage('Quantity must be at least 1'),
  check('rentalPrice').isFloat({ min: 0 }).withMessage('Rental price must be a positive number')
];

const validateEvent = [
  check('title').not().isEmpty().withMessage('Event title is required'),
  check('date').isISO8601().withMessage('Valid date is required'),
  check('venueId').not().isEmpty().withMessage('Venue ID is required'),
  check('organizer').not().isEmpty().withMessage('Organizer is required')
];

// Routes
// Attendee routes
app.post('/api/attendees', validateAttendee, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const attendee = new Attendee(req.body);
    await attendee.save();
    res.status(201).json(attendee);
  } catch (err) {
    if (err.code === 11000) {
      res.status(400).json({ error: 'Email already exists for this event' });
    } else {
      res.status(500).json({ error: 'Server error' });
    }
  }
});

app.get('/api/attendees/:eventId', async (req, res) => {
  try {
    const attendees = await Attendee.find({ eventId: req.params.eventId });
    res.json(attendees);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.put('/api/attendees/:id/checkin', async (req, res) => {
  try {
    const attendee = await Attendee.findByIdAndUpdate(
      req.params.id,
      { checkInStatus: true },
      { new: true }
    );
    if (!attendee) {
      return res.status(404).json({ error: 'Attendee not found' });
    }
    res.json(attendee);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Venue routes
app.post('/api/venues', validateVenue, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const venue = new Venue(req.body);
    await venue.save();
    res.status(201).json(venue);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/api/venues', async (req, res) => {
  try {
    const venues = await Venue.find();
    res.json(venues);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/api/venues/available', async (req, res) => {
  try {
    const { date } = req.query;
    if (!date) {
      return res.status(400).json({ error: 'Date parameter is required' });
    }

    const queryDate = new Date(date);
    const venues = await Venue.find({
      bookedDates: { $not: { $elemMatch: { $eq: queryDate } } }
    });
    res.json(venues);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Equipment routes
app.post('/api/equipment', validateEquipment, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const equipment = new Equipment(req.body);
    await equipment.save();
    res.status(201).json(equipment);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/api/equipment', async (req, res) => {
  try {
    const equipment = await Equipment.find();
    res.json(equipment);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/api/equipment/available', async (req, res) => {
  try {
    const { date } = req.query;
    if (!date) {
      return res.status(400).json({ error: 'Date parameter is required' });
    }

    const queryDate = new Date(date);
    const equipment = await Equipment.find({
      bookedDates: { $not: { $elemMatch: { $eq: queryDate } } }
    });
    res.json(equipment);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Event routes
app.post('/api/events', validateEvent, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    // Check venue availability
    const venue = await Venue.findById(req.body.venueId);
    if (!venue) {
      return res.status(404).json({ error: 'Venue not found' });
    }

    const eventDate = new Date(req.body.date);
    if (venue.bookedDates.some(date => date.getTime() === eventDate.getTime())) {
      return res.status(400).json({ error: 'Venue already booked for this date' });
    }

    // Check equipment availability
    if (req.body.equipmentIds && req.body.equipmentIds.length > 0) {
      const equipment = await Equipment.find({ _id: { $in: req.body.equipmentIds
