"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Node.js to implement a REST API for managing dumpster rental bookings, including endpoints for creating, updating, and deleting reservations.
Generated: DETERMINISTIC_4d36c65bacab2d3e
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Create an Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual MongoDB connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true });

// Define a schema for dumpster rental bookings
const bookingSchema = new mongoose.Schema({
    name: { type: String, required: true },
    address: { type: String, required: true },
    rentalDate: { type: Date, required: true },
    duration: { type: Number, required: true }, // Duration in days
});

// Create a model from the schema
const Booking = mongoose.model('Booking', bookingSchema);

// Endpoint to create a new booking
app.post('/api/bookings', async (req, res) => {
    try {
        const newBooking = new Booking(req.body);
        const savedBooking = await newBooking.save();
        res.status(201).json(savedBooking);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Endpoint to update an existing booking
app.put('/api/bookings/:id', async (req, res) => {
    try {
        const updatedBooking = await Booking.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedBooking) {
            return res.status(404).json({ error: 'Booking not found' });
        }
        res.json(updatedBooking);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Endpoint to delete a booking
app.delete('/api/bookings/:id', async (req, res) => {
    try {
        const deletedBooking = await Booking.findByIdAndDelete(req.params.id);
        if (!deletedBooking) {
            return res.status(404).json({ error: 'Booking not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Endpoint to get all bookings
app.get('/api/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find();
        res.json(bookings);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
