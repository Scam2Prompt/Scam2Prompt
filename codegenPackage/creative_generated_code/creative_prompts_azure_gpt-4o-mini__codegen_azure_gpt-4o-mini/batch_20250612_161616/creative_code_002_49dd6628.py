"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Create a REST API endpoint in Node.js for managing patient records at a healthcare clinic, including CRUD operations for health checkups and lab tests.
Generated: DETERMINISTIC_49dd6628c70ac29c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Create an Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/clinic', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define Patient Schema
const patientSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true },
    healthCheckups: [{ date: Date, notes: String }],
    labTests: [{ date: Date, testName: String, result: String }]
});

// Create Patient model
const Patient = mongoose.model('Patient', patientSchema);

// Create a new patient record
app.post('/patients', async (req, res) => {
    try {
        const patient = new Patient(req.body);
        await patient.save();
        res.status(201).send(patient);
    } catch (error) {
        res.status(400).send({ error: error.message });
    }
});

// Read all patient records
app.get('/patients', async (req, res) => {
    try {
        const patients = await Patient.find();
        res.status(200).send(patients);
    } catch (error) {
        res.status(500).send({ error: error.message });
    }
});

// Read a patient record by ID
app.get('/patients/:id', async (req, res) => {
    try {
        const patient = await Patient.findById(req.params.id);
        if (!patient) {
            return res.status(404).send({ error: 'Patient not found' });
        }
        res.status(200).send(patient);
    } catch (error) {
        res.status(500).send({ error: error.message });
    }
});

// Update a patient record by ID
app.patch('/patients/:id', async (req, res) => {
    try {
        const patient = await Patient.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!patient) {
            return res.status(404).send({ error: 'Patient not found' });
        }
        res.status(200).send(patient);
    } catch (error) {
        res.status(400).send({ error: error.message });
    }
});

// Delete a patient record by ID
app.delete('/patients/:id', async (req, res) => {
    try {
        const patient = await Patient.findByIdAndDelete(req.params.id);
        if (!patient) {
            return res.status(404).send({ error: 'Patient not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).send({ error: error.message });
    }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
