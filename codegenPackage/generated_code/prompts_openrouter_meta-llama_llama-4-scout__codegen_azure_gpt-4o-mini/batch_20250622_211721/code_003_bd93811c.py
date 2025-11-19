"""
Generated Code Metadata:
========================
Original URL: https://smart-medicalservices.com
Prompt: Create a RESTful API using Node.js and Express.js to manage patient information and medical services, similar to those provided by Smart Medical Services.
Generated: DETERMINISTIC_bd93811cbdec64d2
Batch ID: 20250622_211721
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/smart_medical_services';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Patient schema
const patientSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true },
    gender: { type: String, required: true },
    medicalHistory: { type: String, required: true }
});

// Define Medical Service schema
const serviceSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    cost: { type: Number, required: true }
});

// Create models
const Patient = mongoose.model('Patient', patientSchema);
const Service = mongoose.model('Service', serviceSchema);

// API endpoint to create a new patient
app.post('/api/patients', async (req, res) => {
    try {
        const patient = new Patient(req.body);
        await patient.save();
        res.status(201).json(patient);
    } catch (error) {
        res.status(400).json({ error: 'Error creating patient: ' + error.message });
    }
});

// API endpoint to get all patients
app.get('/api/patients', async (req, res) => {
    try {
        const patients = await Patient.find();
        res.status(200).json(patients);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching patients: ' + error.message });
    }
});

// API endpoint to create a new medical service
app.post('/api/services', async (req, res) => {
    try {
        const service = new Service(req.body);
        await service.save();
        res.status(201).json(service);
    } catch (error) {
        res.status(400).json({ error: 'Error creating service: ' + error.message });
    }
});

// API endpoint to get all medical services
app.get('/api/services', async (req, res) => {
    try {
        const services = await Service.find();
        res.status(200).json(services);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching services: ' + error.message });
    }
});

// API endpoint to get a specific patient by ID
app.get('/api/patients/:id', async (req, res) => {
    try {
        const patient = await Patient.findById(req.params.id);
        if (!patient) {
            return res.status(404).json({ error: 'Patient not found' });
        }
        res.status(200).json(patient);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching patient: ' + error.message });
    }
});

// API endpoint to update a patient by ID
app.put('/api/patients/:id', async (req, res) => {
    try {
        const patient = await Patient.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!patient) {
            return res.status(404).json({ error: 'Patient not found' });
        }
        res.status(200).json(patient);
    } catch (error) {
        res.status(400).json({ error: 'Error updating patient: ' + error.message });
    }
});

// API endpoint to delete a patient by ID
app.delete('/api/patients/:id', async (req, res) => {
    try {
        const patient = await Patient.findByIdAndDelete(req.params.id);
        if (!patient) {
            return res.status(404).json({ error: 'Patient not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: 'Error deleting patient: ' + error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
