"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Create a RESTful API using Node.js to handle requests for mobile windscreen repair services, including endpoints for booking appointments and providing service quotes.
Generated: DETERMINISTIC_9d9741b4c39c4196
Batch ID: 20250622_204944
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
mongoose.connect('mongodb://localhost:27017/windscreenRepair', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose Schemas
const appointmentSchema = new mongoose.Schema({
  appointmentId: { type: String, default: uuidv4 },
  customerName: { type: String, required: true },
  contactNumber: { type: String, required: true },
  vehicleMake: { type: String, required: true },
  vehicleModel: { type: String, required: true },
  vehicleYear: { type: Number, required: true },
  damageType: { type: String, required: true },
  appointmentDate: { type: Date, required: true },
  location: { type: String, required: true },
  status: { type: String, default: 'Pending' },
  createdAt: { type: Date, default: Date.now }
});

const quoteSchema = new mongoose.Schema({
  quoteId: { type: String, default: uuidv4 },
  customerName: { type: String, required: true },
  contactNumber: { type: String, required: true },
  vehicleMake: { type: String, required: true },
  vehicleModel: { type: String, required: true },
  vehicleYear: { type: Number, required: true },
  damageType: { type: String, required: true },
  estimatedCost: { type: Number, required: true },
  estimatedTime: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

// Create Mongoose Models
const Appointment = mongoose.model('Appointment', appointmentSchema);
const Quote = mongoose.model('Quote', quoteSchema);

// API Routes

/**
 * @route GET /api/health
 * @description Health check endpoint
 */
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Service is running' });
});

/**
 * @route POST /api/appointments
 * @description Create a new appointment
 */
app.post('/api/appointments', async (req, res) => {
  try {
    const {
      customerName,
      contactNumber,
      vehicleMake,
      vehicleModel,
      vehicleYear,
      damageType,
      appointmentDate,
      location
    } = req.body;

    if (!customerName || !contactNumber || !vehicleMake || !vehicleModel || 
        !vehicleYear || !damageType || !appointmentDate || !location) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const appointment = new Appointment({
      customerName,
      contactNumber,
      vehicleMake,
      vehicleModel,
      vehicleYear,
      damageType,
      appointmentDate,
      location
    });

    await appointment.save();
    res.status(201).json(appointment);
  } catch (error) {
    console.error('Error creating appointment:', error);
    res.status(500).json({ error: 'Failed to create appointment' });
  }
});

/**
 * @route GET /api/appointments
 * @description Get all appointments
 */
app.get('/api/appointments', async (req, res) => {
  try {
    const appointments = await Appointment.find().sort({ createdAt: -1 });
    res.status(200).json(appointments);
  } catch (error) {
    console.error('Error fetching appointments:', error);
    res.status(500).json({ error: 'Failed to fetch appointments' });
  }
});

/**
 * @route GET /api/appointments/:id
 * @description Get a single appointment by ID
 */
app.get('/api/appointments/:id', async (req, res) => {
  try {
    const appointment = await Appointment.findOne({ appointmentId: req.params.id });
    if (!appointment) {
      return res.status(404).json({ error: 'Appointment not found' });
    }
    res.status(200).json(appointment);
  } catch (error) {
    console.error('Error fetching appointment:', error);
    res.status(500).json({ error: 'Failed to fetch appointment' });
  }
});

/**
 * @route POST /api/quotes
 * @description Create a new quote
 */
app.post('/api/quotes', async (req, res) => {
  try {
    const {
      customerName,
      contactNumber,
      vehicleMake,
      vehicleModel,
      vehicleYear,
      damageType,
      estimatedCost,
      estimatedTime
    } = req.body;

    if (!customerName || !contactNumber || !vehicleMake || !vehicleModel || 
        !vehicleYear || !damageType || !estimatedCost || !estimatedTime) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const quote = new Quote({
      customerName,
      contactNumber,
      vehicleMake,
      vehicleModel,
      vehicleYear,
      damageType,
      estimatedCost,
      estimatedTime
    });

    await quote.save();
    res.status(201).json(quote);
  } catch (error) {
    console.error('Error creating quote:', error);
    res.status(500).json({ error: 'Failed to create quote' });
  }
});

/**
 * @route GET /api/quotes
 * @description Get all quotes
 */
app.get('/api/quotes', async (req, res) => {
  try {
    const quotes = await Quote.find().sort({ createdAt: -1 });
    res.status(200).json(quotes);
  } catch (error) {
    console.error('Error fetching quotes:', error);
    res.status(500).json({ error: 'Failed to fetch quotes' });
  }
});

/**
 * @route GET /api/quotes/:id
 * @description Get a single quote by ID
 */
app.get('/api/quotes/:id', async (req, res) => {
  try {
    const quote = await Quote.findOne({ quoteId: req.params.id });
    if (!quote) {
      return res.status(404).json({ error: 'Quote not found' });
    }
    res.status(200).json(quote);
  } catch (error) {
    console.error('Error fetching quote:', error);
    res.status(500).json({ error: 'Failed to fetch quote' });
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
