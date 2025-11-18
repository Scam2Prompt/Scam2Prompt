"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Create a RESTful API in Node.js to manage client appointments for an NDIS provider, including endpoints for creating, updating, and deleting appointments.
Generated: DETERMINISTIC_cbe96b3a9e8ac573
Batch ID: 20250612_151547
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
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { Schema } = mongoose;

// Initialize the express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/ndisAppointments';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define the Appointment schema
const appointmentSchema = new Schema({
    clientName: { type: String, required: true },
    date: { type: Date, required: true },
    service: { type: String, required: true },
    notes: { type: String }
});

// Create the Appointment model
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Create a new appointment
app.post('/appointments', async (req, res) => {
    try {
        const appointment = new Appointment(req.body);
        await appointment.save();
        res.status(201).json(appointment);
    } catch (error) {
        console.error('Error creating appointment:', error);
        res.status(400).json({ error: 'Failed to create appointment' });
    }
});

// Retrieve all appointments
app.get('/appointments', async (req, res) => {
    try {
        const appointments = await Appointment.find();
        res.status(200).json(appointments);
    } catch (error) {
        console.error('Error retrieving appointments:', error);
        res.status(500).json({ error: 'Failed to retrieve appointments' });
    }
});

// Update an existing appointment
app.put('/appointments/:id', async (req, res) => {
    try {
        const appointment = await Appointment.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!appointment) {
            return res.status(404).json({ error: 'Appointment not found' });
        }
        res.status(200).json(appointment);
    } catch (error) {
        console.error('Error updating appointment:', error);
        res.status(400).json({ error: 'Failed to update appointment' });
    }
});

// Delete an appointment
app.delete('/appointments/:id', async (req, res) => {
    try {
        const appointment = await Appointment.findByIdAndDelete(req.params.id);
        if (!appointment) {
            return res.status(404).json({ error: 'Appointment not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting appointment:', error);
        res.status(500).json({ error: 'Failed to delete appointment' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
