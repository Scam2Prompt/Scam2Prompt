"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Create a RESTful API in Node.js to manage bookings and services for a transportation company, including endpoints for retrieving route information and vehicle details.
Generated: DETERMINISTIC_51bf26168a690b9e
Batch ID: 20250622_212855
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
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas
const vehicleSchema = new mongoose.Schema({
    vehicleId: { type: String, required: true, unique: true },
    type: { type: String, required: true },
    capacity: { type: Number, required: true },
    licensePlate: { type: String, required: true },
    status: { type: String, enum: ['available', 'in-use', 'maintenance'], default: 'available' }
});

const routeSchema = new mongoose.Schema({
    routeId: { type: String, required: true, unique: true },
    origin: { type: String, required: true },
    destination: { type: String, required: true },
    distance: { type: Number, required: true },
    estimatedDuration: { type: Number, required: true },
    stops: [{ type: String }]
});

const bookingSchema = new mongoose.Schema({
    bookingId: { type: String, required: true, unique: true },
    customerName: { type: String, required: true },
    customerEmail: { type: String, required: true },
    routeId: { type: String, required: true },
    vehicleId: { type: String, required: true },
    bookingDate: { type: Date, required: true },
    travelDate: { type: Date, required: true },
    status: { type: String, enum: ['confirmed', 'cancelled', 'completed'], default: 'confirmed' }
});

// Create models
const Vehicle = mongoose.model('Vehicle', vehicleSchema);
const Route = mongoose.model('Route', routeSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// API Routes

// Vehicles endpoints
app.get('/api/vehicles', async (req, res) => {
    try {
        const vehicles = await Vehicle.find();
        res.json(vehicles);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.get('/api/vehicles/:id', async (req, res) => {
    try {
        const vehicle = await Vehicle.findOne({ vehicleId: req.params.id });
        if (!vehicle) return res.status(404).json({ message: 'Vehicle not found' });
        res.json(vehicle);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/vehicles', async (req, res) => {
    try {
        const newVehicle = new Vehicle(req.body);
        const savedVehicle = await newVehicle.save();
        res.status(201).json(savedVehicle);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Routes endpoints
app.get('/api/routes', async (req, res) => {
    try {
        const routes = await Route.find();
        res.json(routes);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.get('/api/routes/:id', async (req, res) => {
    try {
        const route = await Route.findOne({ routeId: req.params.id });
        if (!route) return res.status(404).json({ message: 'Route not found' });
        res.json(route);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/routes', async (req, res) => {
    try {
        const newRoute = new Route(req.body);
        const savedRoute = await newRoute.save();
        res.status(201).json(savedRoute);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Bookings endpoints
app.get('/api/bookings', async (req, res) => {
    try {
        const bookings = await Booking.find().populate('routeId').populate('vehicleId');
        res.json(bookings);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.get('/api/bookings/:id', async (req, res) => {
    try {
        const booking = await Booking.findOne({ bookingId: req.params.id })
            .populate('routeId')
            .populate('vehicleId');
        if (!booking) return res.status(404).json({ message: 'Booking not found' });
        res.json(booking);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/bookings', async (req, res) => {
    try {
        const newBooking = new Booking(req.body);
        const savedBooking = await newBooking.save();
        res.status(201).json(savedBooking);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.put('/api/bookings/:id', async (req, res) => {
    try {
        const updatedBooking = await Booking.findOneAndUpdate(
            { bookingId: req.params.id },
            req.body,
            { new: true }
        );
        if (!updatedBooking) return res.status(404).json({ message: 'Booking not found' });
        res.json(updatedBooking);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
