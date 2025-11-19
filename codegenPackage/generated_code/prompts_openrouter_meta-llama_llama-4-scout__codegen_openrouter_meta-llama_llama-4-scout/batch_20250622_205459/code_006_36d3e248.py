"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Generate a code snippet in JavaScript to create a simple patient portal for a breast care center, including features like appointment scheduling and medical records access.
Generated: DETERMINISTIC_36d3e2488d3466ff
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// patientPortal.js

/**
 * Patient Portal for Breast Care Center
 * 
 * This module provides a simple patient portal with features like appointment scheduling and medical records access.
 */

// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/breastCareCenter', { useNewUrlParser: true, useUnifiedTopology: true });

// Define patient schema
const patientSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String,
    medicalRecords: [{ type: mongoose.Schema.Types.ObjectId, ref: 'MedicalRecord' }],
    appointments: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Appointment' }]
});

// Define medical record schema
const medicalRecordSchema = new mongoose.Schema({
    patientId: { type: mongoose.Schema.Types.ObjectId, ref: 'Patient' },
    recordDate: Date,
    description: String
});

// Define appointment schema
const appointmentSchema = new mongoose.Schema({
    patientId: { type: mongoose.Schema.Types.ObjectId, ref: 'Patient' },
    appointmentDate: Date,
    description: String
});

// Compile schemas into models
const Patient = mongoose.model('Patient', patientSchema);
const MedicalRecord = mongoose.model('MedicalRecord', medicalRecordSchema);
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Express middleware to parse JSON bodies
app.use(express.json());

// Register patient
app.post('/register', async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 10);
        const patient = new Patient({
            name: req.body.name,
            email: req.body.email,
            password: hashedPassword
        });
        await patient.save();
        res.status(201).send({ message: 'Patient registered successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error registering patient', error });
    }
});

// Login patient
app.post('/login', async (req, res) => {
    try {
        const patient = await Patient.findOne({ email: req.body.email });
        if (!patient) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, patient.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ patientId: patient._id }, 'secretKey', { expiresIn: '1h' });
        res.send({ token });
    } catch (error) {
        res.status(400).send({ message: 'Error logging in patient', error });
    }
});

// Get patient medical records
app.get('/medical-records', authenticateToken, async (req, res) => {
    try {
        const patient = await Patient.findById(req.patientId).populate('medicalRecords');
        res.send(patient.medicalRecords);
    } catch (error) {
        res.status(400).send({ message: 'Error fetching medical records', error });
    }
});

// Schedule appointment
app.post('/appointments', authenticateToken, async (req, res) => {
    try {
        const appointment = new Appointment({
            patientId: req.patientId,
            appointmentDate: req.body.appointmentDate,
            description: req.body.description
        });
        await appointment.save();
        const patient = await Patient.findById(req.patientId);
        patient.appointments.push(appointment._id);
        await patient.save();
        res.status(201).send({ message: 'Appointment scheduled successfully' });
    } catch (error) {
        res.status(400).send({ message: 'Error scheduling appointment', error });
    }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ message: 'Access denied' });
    try {
        const decoded = jwt.verify(token, 'secretKey');
        req.patientId = decoded.patientId;
        next();
    } catch (error) {
        res.status(400).send({ message: 'Invalid token', error });
    }
}

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
