"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Create a RESTful API in Node.js to manage client appointments for an NDIS provider, including endpoints for creating, updating, and deleting appointments.
Generated: DETERMINISTIC_cbe96b3a9e8ac573
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration
let appointments = [];

/**
 * Appointment Model
 * @typedef {Object} Appointment
 * @property {string} id - Unique identifier
 * @property {string} clientId - NDIS client ID
 * @property {string} providerId - Service provider ID
 * @property {string} date - Appointment date (ISO format)
 * @property {string} time - Appointment time
 * @property {string} duration - Duration in minutes
 * @property {string} serviceType - Type of service
 * @property {string} status - Appointment status (e.g., scheduled, completed, cancelled)
 * @property {string} notes - Additional notes
 */

// Helper function to find appointment by ID
const findAppointmentById = (id) => appointments.find(appt => appt.id === id);

// Helper function to validate appointment data
const validateAppointmentData = (data, isUpdate = false) => {
    const requiredFields = ['clientId', 'providerId', 'date', 'time', 'duration', 'serviceType'];
    const errors = [];

    if (!isUpdate) {
        for (const field of requiredFields) {
            if (!data[field]) {
                errors.push(`${field} is required`);
            }
        }
    }

    if (data.date && !Date.parse(data.date)) {
        errors.push('Invalid date format');
    }

    if (data.duration && isNaN(data.duration)) {
        errors.push('Duration must be a number');
    }

    return errors;
};

/**
 * @route GET /api/appointments
 * @description Get all appointments
 * @returns {Appointment[]} List of appointments
 */
app.get('/api/appointments', (req, res) => {
    try {
        res.status(200).json(appointments);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve appointments' });
    }
});

/**
 * @route GET /api/appointments/:id
 * @description Get a single appointment by ID
 * @param {string} id - Appointment ID
 * @returns {Appointment} The requested appointment
 */
app.get('/api/appointments/:id', (req, res) => {
    try {
        const appointment = findAppointmentById(req.params.id);
        if (!appointment) {
            return res.status(404).json({ error: 'Appointment not found' });
        }
        res.status(200).json(appointment);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve appointment' });
    }
});

/**
 * @route POST /api/appointments
 * @description Create a new appointment
 * @param {Appointment} req.body - Appointment data
 * @returns {Appointment} The created appointment
 */
app.post('/api/appointments', (req, res) => {
    try {
        const errors = validateAppointmentData(req.body);
        if (errors.length > 0) {
            return res.status(400).json({ errors });
        }

        const newAppointment = {
            id: uuidv4(),
            clientId: req.body.clientId,
            providerId: req.body.providerId,
            date: req.body.date,
            time: req.body.time,
            duration: req.body.duration,
            serviceType: req.body.serviceType,
            status: req.body.status || 'scheduled',
            notes: req.body.notes || '',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };

        appointments.push(newAppointment);
        res.status(201).json(newAppointment);
    } catch (error) {
        res.status(500).json({ error: 'Failed to create appointment' });
    }
});

/**
 * @route PUT /api/appointments/:id
 * @description Update an existing appointment
 * @param {string} id - Appointment ID
 * @param {Appointment} req.body - Updated appointment data
 * @returns {Appointment} The updated appointment
 */
app.put('/api/appointments/:id', (req, res) => {
    try {
        const appointment = findAppointmentById(req.params.id);
        if (!appointment) {
            return res.status(404).json({ error: 'Appointment not found' });
        }

        const errors = validateAppointmentData(req.body, true);
        if (errors.length > 0) {
            return res.status(400).json({ errors });
        }

        const updatedAppointment = {
            ...appointment,
            ...req.body,
            updatedAt: new Date().toISOString()
        };

        appointments = appointments.map(appt => 
            appt.id === req.params.id ? updatedAppointment : appt
        );

        res.status(200).json(updatedAppointment);
    } catch (error) {
        res.status(500).json({ error: 'Failed to update appointment' });
    }
});

/**
 * @route DELETE /api/appointments/:id
 * @description Delete an appointment
 * @param {string} id - Appointment ID
 * @returns {Object} Success message
 */
app.delete('/api/appointments/:id', (req, res) => {
    try {
        const appointment = findAppointmentById(req.params.id);
        if (!appointment) {
            return res.status(404).json({ error: 'Appointment not found' });
        }

        appointments = appointments.filter(appt => appt.id !== req.params.id);
        res.status(200).json({ message: 'Appointment deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to delete appointment' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
