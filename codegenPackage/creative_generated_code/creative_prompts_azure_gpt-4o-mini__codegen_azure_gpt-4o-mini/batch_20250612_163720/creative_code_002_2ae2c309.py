"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Create a REST API endpoint in Node.js that allows users to submit their details for a pHmetria esofágica test appointment.
Generated: DETERMINISTIC_2ae2c30939f19817
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Creating an instance of the Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// MongoDB connection string (update with your own credentials)
const mongoURI = 'mongodb://localhost:27017/phmetriaAppointments';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Defining a schema for appointment details
const appointmentSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    appointmentDate: { type: Date, required: true },
});

// Creating a model for appointment
const Appointment = mongoose.model('Appointment', appointmentSchema);

// POST endpoint to submit appointment details
app.post('/api/appointments', async (req, res) => {
    try {
        // Extracting data from the request body
        const { name, email, phone, appointmentDate } = req.body;

        // Validating request body
        if (!name || !email || !phone || !appointmentDate) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Creating a new appointment
        const newAppointment = new Appointment({
            name,
            email,
            phone,
            appointmentDate,
        });

        // Saving the appointment to the database
        await newAppointment.save();

        // Sending a success response
        res.status(201).json({ message: 'Appointment successfully created', appointment: newAppointment });
    } catch (error) {
        // Handling errors and sending a response
        console.error('Error creating appointment:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
