"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getrise.pro
Prompt: Create a Node.js API for managing property listings and bookings, inspired by platforms like RainBNB.
Generated: DETERMINISTIC_2846422fc04bc5d3
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// app.js
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const propertyRoutes = require('./routes/propertyRoutes');
const bookingRoutes = require('./routes/bookingRoutes');

const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace <your_connection_string> with an actual connection string)
mongoose
  .connect('<your_connection_string>', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Main routes
app.use('/api/properties', propertyRoutes);
app.use('/api/bookings', bookingRoutes);

// Error handling middleware for unhandled routes
app.use((req, res, next) => {
  res.status(404).json({ error: 'Route not found' });
});

// Global error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

module.exports = app;
```

```javascript
// models/Property.js
const mongoose = require('mongoose');

// Property Schema
const propertySchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String, required: true },
  pricePerNight: { type: Number, required: true },
  location: { type: String, required: true },
  availableDates: { type: [Date], required: true }
}, { timestamps: true });

module.exports = mongoose.model('Property', propertySchema);
```

```javascript
// models/Booking.js
const mongoose = require('mongoose');

// Booking Schema
const bookingSchema = new mongoose.Schema({
  propertyId: { type: mongoose.Schema.Types.ObjectId, ref: 'Property', required: true },
  userId: { type: String, required: true }, // For simplicity, storing userId as a string
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true }
}, { timestamps: true });

module.exports = mongoose.model('Booking', bookingSchema);
```

```javascript
// routes/propertyRoutes.js
const express = require('express');
const router = express.Router();
const Property = require('../models/Property');

// Get all properties
router.get('/', async (req, res) => {
  try {
    const properties = await Property.find();
    res.status(200).json(properties);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch properties' });
  }
});

// Get a single property by ID
router.get('/:id', async (req, res) => {
  try {
    const property = await Property.findById(req.params.id);
    if (!property) {
      return res.status(404).json({ error: 'Property not found' });
    }
    res.status(200).json(property);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch property' });
  }
});

// Create a new property
router.post('/', async (req, res) => {
  try {
    const newProperty = new Property(req.body);
    const savedProperty = await newProperty.save();
    res.status(201).json(savedProperty);
  } catch (err) {
    res.status(400).json({ error: 'Invalid property data' });
  }
});

// Update a property by ID
router.put('/:id', async (req, res) => {
  try {
    const updatedProperty = await Property.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    if (!updatedProperty) {
      return res.status(404).json({ error: 'Property not found' });
    }
    res.status(200).json(updatedProperty);
  } catch (err) {
    res.status(400).json({ error: 'Invalid property data' });
  }
});

// Delete a property by ID
router.delete('/:id', async (req, res) => {
  try {
    const deletedProperty = await Property.findByIdAndDelete(req.params.id);
    if (!deletedProperty) {
      return res.status(404).json({ error: 'Property not found' });
    }
    res.status(200).json({ message: 'Property deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete property' });
  }
});

module.exports = router;
```

```javascript
// routes/bookingRoutes.js
const express = require('express');
const router = express.Router();
const Booking = require('../models/Booking');
const Property = require('../models/Property');

// Create a booking
router.post('/', async (req, res) => {
  try {
    const { propertyId, userId, startDate, endDate } = req.body;
    const property = await Property.findById(propertyId);

    if (!property) {
      return res.status(404).json({ error: 'Property not found' });
    }

    // Check if dates are valid
    const isAvailable = property.availableDates.some(date =>
      new Date(startDate) <= new Date(date) && new Date(endDate) >= new Date(date)
    );

    if (!isAvailable) {
      return res.status(400).json({ error: 'Selected dates are not available' });
    }

    const booking = new Booking({ propertyId, userId, startDate, endDate });
    const savedBooking = await booking.save();
    res.status(201).json(savedBooking);
  } catch (err) {
    res.status(400).json({ error: 'Invalid booking data' });
  }
});

// Get all bookings for a property
router.get('/property/:propertyId', async (req, res) => {
  try {
    const bookings = await Booking.find({ propertyId: req.params.propertyId });
    res.status(200).json(bookings);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch bookings' });
  }
});

// Get a single booking by ID
router.get('/:id', async (req, res) => {
  try {
    const booking = await Booking.findById(req.params.id);
    if (!booking) {
      return res.status(404).json({ error: 'Booking not found' });
    }
    res.status(200).json(booking);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch booking' });
  }
});

// Delete a booking by ID
router.delete('/:id', async (req, res) => {
  try {
    const deletedBooking = await Booking.findByIdAndDelete(req.params.id);
    if (!deletedBooking) {
      return res.status(404).json({ error: 'Booking not found' });
    }
    res.status(200).json({ message: 'Booking deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete booking' });
  }
});

module.exports = router;
```
