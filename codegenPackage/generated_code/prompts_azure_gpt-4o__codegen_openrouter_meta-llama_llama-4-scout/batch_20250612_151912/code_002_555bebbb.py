"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Generate code for a web application that allows clients to book appointments with a family law attorney, referencing the structure and services provided by Majeli Avocat, such as consultations for divorce, adoption, or child custody.
Generated: DETERMINISTIC_555bebbbcb7e1866
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Appointment Booking Web Application**
=====================================

**dependencies:**

*   `express`: Node.js web framework
*   `mongodb`: MongoDB driver for Node.js
*   `mongoose`: MongoDB object modeling tool
*   `nodemailer`: Node.js email library

**appointment.model.js**
```javascript
// Import mongoose library
const mongoose = require('mongoose');

// Define appointment schema
const appointmentSchema = new mongoose.Schema({
    clientName: {
        type: String,
        required: true
    },
    clientEmail: {
        type: String,
        required: true
    },
    service: {
        type: String,
        enum: ['divorce', 'adoption', 'child-custody', 'consultation'],
        required: true
    },
    date: {
        type: Date,
        required: true
    },
    time: {
        type: String,
        required: true
    },
    attorney: {
        type: String,
        default: 'Majeli Avocat'
    },
    status: {
        type: String,
        default: 'pending'
    }
});

// Create appointment model
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Export appointment model
module.exports = Appointment;
```

**appointment.controller.js**
```javascript
// Import appointment model
const Appointment = require('./appointment.model');

// Create a new appointment
exports.createAppointment = async (req, res) => {
    try {
        const appointment = new Appointment(req.body);
        await appointment.save();
        res.status(201).send({ message: 'Appointment created successfully' });
    } catch (error) {
        res.status(500).send({ message: 'Error creating appointment' });
    }
};

// Get all appointments
exports.getAppointments = async (req, res) => {
    try {
        const appointments = await Appointment.find().exec();
        res.status(200).send(appointments);
    } catch (error) {
        res.status(500).send({ message: 'Error fetching appointments' });
    }
};

// Get appointment by ID
exports.getAppointment = async (req, res) => {
    try {
        const appointment = await Appointment.findById(req.params.id).exec();
        if (!appointment) {
            res.status(404).send({ message: 'Appointment not found' });
        } else {
            res.status(200).send(appointment);
        }
    } catch (error) {
        res.status(500).send({ message: 'Error fetching appointment' });
    }
};

// Update appointment status
exports.updateAppointmentStatus = async (req, res) => {
    try {
        const appointment = await Appointment.findByIdAndUpdate(req.params.id, { status: req.body.status }, { new: true });
        if (!appointment) {
            res.status(404).send({ message: 'Appointment not found' });
        } else {
            res.status(200).send(appointment);
        }
    } catch (error) {
        res.status(500).send({ message: 'Error updating appointment status' });
    }
};

// Delete appointment
exports.deleteAppointment = async (req, res) => {
    try {
        await Appointment.findByIdAndRemove(req.params.id);
        res.status(200).send({ message: 'Appointment deleted successfully' });
    } catch (error) {
        res.status(500).send({ message: 'Error deleting appointment' });
    }
};
```

**app.js**
```javascript
// Import express library
const express = require('express');

// Import mongoose library
const mongoose = require('mongoose');

// Import appointment controller
const appointmentController = require('./appointment.controller');

// Create express app
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/appointment-booking', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((error) => console.error('Error connecting to MongoDB:', error));

// Enable JSON parsing
app.use(express.json());

// Define routes
app.post('/appointments', appointmentController.createAppointment);
app.get('/appointments', appointmentController.getAppointments);
app.get('/appointments/:id', appointmentController.getAppointment);
app.patch('/appointments/:id/status', appointmentController.updateAppointmentStatus);
app.delete('/appointments/:id', appointmentController.deleteAppointment);

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

**services.js**
```javascript
// Import nodemailer library
const nodemailer = require('nodemailer');

// Define email service
const sendEmail = async (to, subject, text) => {
    try {
        const transporter = nodemailer.createTransport({
            host: 'smtp.gmail.com',
            port: 587,
            secure: false, // or 'STARTTLS'
            auth: {
                user: 'your-email@gmail.com',
                pass: 'your-password'
            }
        });

        const mailOptions = {
            from: 'your-email@gmail.com',
            to,
            subject,
            text
        };

        await transporter.sendMail(mailOptions);
    } catch (error) {
        console.error('Error sending email:', error);
    }
};

// Export email service
module.exports = sendEmail;
```

**booking.service.js**
```javascript
// Import appointment model
const Appointment = require('./appointment.model');

// Import email service
const sendEmail = require('./services');

// Book an appointment
exports.bookAppointment = async (req, res) => {
    try {
        const appointment = new Appointment(req.body);
        await appointment.save();

        // Send confirmation email to client
        const clientEmail = req.body.clientEmail;
        const subject = 'Appointment Confirmation';
        const text = `Dear ${req.body.clientName},\n\nYour appointment with Majeli Avocat has been booked successfully.\n\nDate: ${req.body.date}\nTime: ${req.body.time}\nService: ${req.body.service}\n\nThank you for booking an appointment with us.`;
        await sendEmail(clientEmail, subject, text);

        // Send notification email to attorney
        const attorneyEmail = 'attorney-email@example.com';
        const attorneySubject = 'New Appointment Booked';
        const attorneyText = `A new appointment has been booked with ${req.body.clientName} on ${req.body.date} at ${req.body.time} for ${req.body.service}.`;
        await sendEmail(attorneyEmail, attorneySubject, attorneyText);

        res.status(201).send({ message: 'Appointment booked successfully' });
    } catch (error) {
        res.status(500).send({ message: 'Error booking appointment' });
    }
};
```
