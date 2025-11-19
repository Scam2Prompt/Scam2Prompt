"""
Generated Code Metadata:
========================
Original URL: https://lgin-uphoiolds.godaddysites.com
Prompt: Design a booking system API using Node.js and Express that can handle requests similar to the "Book Now" functionality on the given website.
Generated: DETERMINISTIC_a52f4d3c61d17dda
Batch ID: 20250622_212843
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
const moment = require('moment');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/booking-system', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for Booking model
const bookingSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    phone: { type: String, required: true },
    service: { type: String, required: true },
    date: { type: Date, required: true },
    time: { type: String, required: true },
});

// Create Booking model
const Booking = mongoose.model('Booking', bookingSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new booking
/**
 * @api {post} /bookings Create Booking
 * @apiBody {String} name Customer name
 * @apiBody {String} email Customer email
 * @apiBody {String} phone Customer phone
 * @apiBody {String} service Service to book
 * @apiBody {Date} date Booking date
 * @apiBody {String} time Booking time
 * @apiSuccess {Object} booking Created booking
 */
app.post('/bookings', async (req, res) => {
    try {
        const { name, email, phone, service, date, time } = req.body;

        // Validate request body
        if (!name || !email || !phone || !service || !date || !time) {
            return res.status(400).json({ error: 'Please provide all required fields' });
        }

        // Check if date is valid
        const bookingDate = moment(date).toDate();
        if (moment(bookingDate).isBefore(moment())) {
            return res.status(400).json({ error: 'Booking date must be in the future' });
        }

        // Create new booking
        const booking = new Booking({ name, email, phone, service, date: bookingDate, time });
        await booking.save();

        // Return created booking
        res.json(booking);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to create booking' });
    }
});

// API endpoint to get all bookings
/**
 * @api {get} /bookings Get All Bookings
 * @apiSuccess {Array} bookings List of bookings
 */
app.get('/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find().exec();
        res.json(bookings);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to retrieve bookings' });
    }
});

// API endpoint to get a booking by ID
/**
 * @api {get} /bookings/:id Get Booking
 * @apiParam {String} id Booking ID
 * @apiSuccess {Object} booking Booking details
 */
app.get('/bookings/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const booking = await Booking.findById(id).exec();

        if (!booking) {
            return res.status(404).json({ error: 'Booking not found' });
        }

        res.json(booking);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to retrieve booking' });
    }
});

// API endpoint to update a booking
/**
 * @api {patch} /bookings/:id Update Booking
 * @apiParam {String} id Booking ID
 * @apiBody {String} [name] Customer name
 * @apiBody {String} [email] Customer email
 * @apiBody {String} [phone] Customer phone
 * @apiBody {String} [service] Service to book
 * @apiBody {Date} [date] Booking date
 * @apiBody {String} [time] Booking time
 * @apiSuccess {Object} booking Updated booking
 */
app.patch('/bookings/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const updates = req.body;

        // Validate updates
        if (updates.date) {
            const bookingDate = moment(updates.date).toDate();
            if (moment(bookingDate).isBefore(moment())) {
                return res.status(400).json({ error: 'Booking date must be in the future' });
            }
        }

        const booking = await Booking.findByIdAndUpdate(id, updates, { new: true }).exec();

        if (!booking) {
            return res.status(404).json({ error: 'Booking not found' });
        }

        res.json(booking);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to update booking' });
    }
});

// API endpoint to delete a booking
/**
 * @api {delete} /bookings/:id Delete Booking
 * @apiParam {String} id Booking ID
 * @apiSuccess {Object} message Deletion confirmation
 */
app.delete('/bookings/:id', async (req, res) => {
    try {
        const id = req.params.id;
        await Booking.findByIdAndRemove(id).exec();
        res.json({ message: 'Booking deleted successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to delete booking' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
