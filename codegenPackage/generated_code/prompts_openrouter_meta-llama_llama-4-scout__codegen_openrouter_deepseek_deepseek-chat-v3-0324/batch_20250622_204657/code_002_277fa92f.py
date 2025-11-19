"""
Generated Code Metadata:
========================
Original URL: https://xn--strkfysioterapi-ylb.no
Prompt: Generate a RESTful API endpoint in Node.js for managing physiotherapy session bookings, including patient and therapist information.
Generated: DETERMINISTIC_277fa92f81f8ff99
Batch ID: 20250622_204657
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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database connection
mongoose.connect('mongodb://localhost:27017/physiotherapyDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('Database connection error:', err);
});

// Define Mongoose Schemas
const patientSchema = new mongoose.Schema({
    patientId: { type: String, default: uuidv4, unique: true },
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    address: { type: String },
    medicalHistory: { type: String },
    createdAt: { type: Date, default: Date.now }
});

const therapistSchema = new mongoose.Schema({
    therapistId: { type: String, default: uuidv4, unique: true },
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    specialization: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

const bookingSchema = new mongoose.Schema({
    bookingId: { type: String, default: uuidv4, unique: true },
    patientId: { type: String, required: true },
    therapistId: { type: String, required: true },
    sessionDate: { type: Date, required: true },
    sessionTime: { type: String, required: true },
    duration: { type: Number, required: true }, // in minutes
    status: { type: String, enum: ['scheduled', 'completed', 'cancelled'], default: 'scheduled' },
    notes: { type: String },
    createdAt: { type: Date, default: Date.now }
});

// Create Mongoose Models
const Patient = mongoose.model('Patient', patientSchema);
const Therapist = mongoose.model('Therapist', therapistSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// API Endpoints

// Create a new patient
app.post('/api/patients', async (req, res) => {
    try {
        const patient = new Patient(req.body);
        await patient.save();
        res.status(201).json(patient);
    } catch (err) {
        if (err.name === 'ValidationError') {
            res.status(400).json({ error: err.message });
        } else if (err.code === 11000) {
            res.status(400).json({ error: 'Email already exists' });
        } else {
            res.status(500).json({ error: 'Server error' });
        }
    }
});

// Get all patients
app.get('/api/patients', async (req, res) => {
    try {
        const patients = await Patient.find();
        res.json(patients);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Create a new therapist
app.post('/api/therapists', async (req, res) => {
    try {
        const therapist = new Therapist(req.body);
        await therapist.save();
        res.status(201).json(therapist);
    } catch (err) {
        if (err.name === 'ValidationError') {
            res.status(400).json({ error: err.message });
        } else if (err.code === 11000) {
            res.status(400).json({ error: 'Email already exists' });
        } else {
            res.status(500).json({ error: 'Server error' });
        }
    }
});

// Get all therapists
app.get('/api/therapists', async (req, res) => {
    try {
        const therapists = await Therapist.find();
        res.json(therapists);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Create a new booking
app.post('/api/bookings', async (req, res) => {
    try {
        // Check if patient exists
        const patient = await Patient.findOne({ patientId: req.body.patientId });
        if (!patient) {
            return res.status(404).json({ error: 'Patient not found' });
        }

        // Check if therapist exists
        const therapist = await Therapist.findOne({ therapistId: req.body.therapistId });
        if (!therapist) {
            return res.status(404).json({ error: 'Therapist not found' });
        }

        // Check for booking conflicts
        const existingBooking = await Booking.findOne({
            therapistId: req.body.therapistId,
            sessionDate: req.body.sessionDate,
            sessionTime: req.body.sessionTime,
            status: { $ne: 'cancelled' }
        });

        if (existingBooking) {
            return res.status(400).json({ error: 'Time slot already booked' });
        }

        const booking = new Booking(req.body);
        await booking.save();
        res.status(201).json(booking);
    } catch (err) {
        if (err.name === 'ValidationError') {
            res.status(400).json({ error: err.message });
        } else {
            res.status(500).json({ error: 'Server error' });
        }
    }
});

// Get all bookings
app.get('/api/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find()
            .populate('patientId', 'name email')
            .populate('therapistId', 'name specialization');
        res.json(bookings);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Update booking status
app.patch('/api/bookings/:id/status', async (req, res) => {
    try {
        const booking = await Booking.findOneAndUpdate(
            { bookingId: req.params.id },
            { status: req.body.status },
            { new: true }
        );

        if (!booking) {
            return res.status(404).json({ error: 'Booking not found' });
        }

        res.json(booking);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Get bookings by patient ID
app.get('/api/patients/:id/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find({ patientId: req.params.id })
            .populate('therapistId', 'name specialization');
        res.json(bookings);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Get bookings by therapist ID
app.get('/api/therapists/:id/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find({ therapistId: req.params.id })
            .populate('patientId', 'name email');
        res.json(bookings);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```
