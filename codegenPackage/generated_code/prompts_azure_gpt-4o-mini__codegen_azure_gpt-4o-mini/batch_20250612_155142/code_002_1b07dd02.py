"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Create a JavaScript application that allows users to book appointments for NDIS services, incorporating the 24x7 support feature highlighted by Shareth Homecare.
Generated: DETERMINISTIC_1b07dd02df2850c8
Batch ID: 20250612_155142
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

# Generated Code:
# ===============

```javascript
// Appointment Booking Application for NDIS Services
// Author: [Your Name]
// Date: [Current Date]

// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const moment = require('moment');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/ndisAppointments', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Appointment Schema
const appointmentSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    service: { type: String, required: true },
    date: { type: Date, required: true },
    time: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create Appointment Model
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Route to book an appointment
app.post('/api/appointments', async (req, res) => {
    try {
        const { name, email, service, date, time } = req.body;

        // Validate input
        if (!name || !email || !service || !date || !time) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Check if the appointment date is in the future
        if (moment(date).isBefore(moment())) {
            return res.status(400).json({ error: 'Appointment date must be in the future' });
        }

        // Create a new appointment
        const newAppointment = new Appointment({ name, email, service, date, time });
        await newAppointment.save();

        // Respond with the created appointment
        res.status(201).json(newAppointment);
    } catch (error) {
        console.error('Error booking appointment:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get all appointments
app.get('/api/appointments', async (req, res) => {
    try {
        const appointments = await Appointment.find();
        res.status(200).json(appointments);
    } catch (error) {
        console.error('Error fetching appointments:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Instructions to Run the Application
1. Ensure you have Node.js and MongoDB installed on your machine.
2. Create a new directory for the project and navigate into it.
3. Run `npm init -y` to create a `package.json` file.
4. Install the required packages by running:
   ```bash
   npm install express body-parser mongoose moment
   ```
5. Save the provided code in a file named `app.js`.
6. Start your MongoDB server.
7. Run the application using:
   ```bash
   node app.js
   ```
8. Use a tool like Postman to test the API endpoints.
