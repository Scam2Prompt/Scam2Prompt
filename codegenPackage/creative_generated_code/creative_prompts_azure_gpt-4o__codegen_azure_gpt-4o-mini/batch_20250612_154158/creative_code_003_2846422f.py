"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getrise.pro
Prompt: Create a Node.js API for managing property listings and bookings, inspired by platforms like RainBNB.
Generated: DETERMINISTIC_2846422fc04bc5d3
Batch ID: 20250612_154158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/rainbnb', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define Property schema
const propertySchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    location: { type: String, required: true },
    price: { type: Number, required: true },
    availableDates: [{ type: Date }],
});

// Define Booking schema
const bookingSchema = new mongoose.Schema({
    propertyId: { type: mongoose.Schema.Types.ObjectId, ref: 'Property', required: true },
    userId: { type: String, required: true },
    startDate: { type: Date, required: true },
    endDate: { type: Date, required: true },
});

// Create models
const Property = mongoose.model('Property', propertySchema);
const Booking = mongoose.model('Booking', bookingSchema);

// Route to create a new property
app.post('/properties', async (req, res) => {
    try {
        const property = new Property(req.body);
        await property.save();
        res.status(201).json(property);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Route to get all properties
app.get('/properties', async (req, res) => {
    try {
        const properties = await Property.find();
        res.status(200).json(properties);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Route to get a specific property by ID
app.get('/properties/:id', async (req, res) => {
    try {
        const property = await Property.findById(req.params.id);
        if (!property) {
            return res.status(404).json({ error: 'Property not found' });
        }
        res.status(200).json(property);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Route to create a booking
app.post('/bookings', async (req, res) => {
    try {
        const booking = new Booking(req.body);
        await booking.save();
        res.status(201).json(booking);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Route to get all bookings
app.get('/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find().populate('propertyId');
        res.status(200).json(bookings);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Route to get bookings for a specific property
app.get('/properties/:id/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find({ propertyId: req.params.id });
        res.status(200).json(bookings);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Handle graceful shutdown
process.on('SIGINT', async () => {
    await mongoose.connection.close();
    process.exit(0);
});
```
