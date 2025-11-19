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
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for patients
const patientSchema = new mongoose.Schema({
  name: String,
  dateOfBirth: Date,
  contactNumber: String,
  medicalHistory: String,
});

// Define schema for medical services
const serviceSchema = new mongoose.Schema({
  name: String,
  description: String,
  cost: Number,
});

// Create models for patients and services
const Patient = mongoose.model('Patient', patientSchema);
const Service = mongoose.model('Service', serviceSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new patient
app.post('/patients', async (req, res) => {
  try {
    const patient = new Patient(req.body);
    await patient.save();
    res.status(201).send(patient);
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to get all patients
app.get('/patients', async (req, res) => {
  try {
    const patients = await Patient.find().exec();
    res.send(patients);
  } catch (error) {
    res.status(500).send({ message: error.message });
  }
});

// API endpoint to get a patient by ID
app.get('/patients/:id', async (req, res) => {
  try {
    const patient = await Patient.findById(req.params.id).exec();
    if (!patient) {
      return res.status(404).send({ message: 'Patient not found' });
    }
    res.send(patient);
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to update a patient
app.put('/patients/:id', async (req, res) => {
  try {
    const patient = await Patient.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!patient) {
      return res.status(404).send({ message: 'Patient not found' });
    }
    res.send(patient);
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to delete a patient
app.delete('/patients/:id', async (req, res) => {
  try {
    await Patient.findByIdAndRemove(req.params.id);
    res.status(204).send();
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to create a new medical service
app.post('/services', async (req, res) => {
  try {
    const service = new Service(req.body);
    await service.save();
    res.status(201).send(service);
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to get all medical services
app.get('/services', async (req, res) => {
  try {
    const services = await Service.find().exec();
    res.send(services);
  } catch (error) {
    res.status(500).send({ message: error.message });
  }
});

// API endpoint to get a medical service by ID
app.get('/services/:id', async (req, res) => {
  try {
    const service = await Service.findById(req.params.id).exec();
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.send(service);
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to update a medical service
app.put('/services/:id', async (req, res) => {
  try {
    const service = await Service.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.send(service);
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// API endpoint to delete a medical service
app.delete('/services/:id', async (req, res) => {
  try {
    await Service.findByIdAndRemove(req.params.id);
    res.status(204).send();
  } catch (error) {
    res.status(400).send({ message: error.message });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// For running this file 
// create .env file 
// DB_URL="mongodb://localhost:27017/mydatabase"
// PORT=3000
// then 
// npm install express mongoose dotenv 
// node index.js 
```
