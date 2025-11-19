"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: "Design a system solution using modern technology tools for a healthcare project, similar to those delivered by DFIVE Technologies."
Generated: DETERMINISTIC_2bf37093b3a824b4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready code example for a healthcare project. The solution uses a modern stack with Node.js, Express.js, and MongoDB for backend development. It includes a RESTful API for managing patient records.

```javascript
// server.js
// Entry point for the healthcare project backend system

// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Database connection error:', err.message);
    process.exit(1); // Exit process if database connection fails
  });

// Define Patient schema and model
const patientSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
  gender: { type: String, required: true },
  contactNumber: { type: String, required: true },
  medicalHistory: { type: [String], default: [] },
}, { timestamps: true });

const Patient = mongoose.model('Patient', patientSchema);

// Routes

// GET /patients - Retrieve all patients
app.get('/patients', async (req, res) => {
  try {
    const patients = await Patient.find();
    res.status(200).json(patients);
  } catch (err) {
    console.error('Error fetching patients:', err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// POST /patients - Add a new patient
app.post('/patients', async (req, res) => {
  try {
    const { name, age, gender, contactNumber, medicalHistory } = req.body;

    // Validate input
    if (!name || !age || !gender || !contactNumber) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const newPatient = new Patient({ name, age, gender, contactNumber, medicalHistory });
    const savedPatient = await newPatient.save();
    res.status(201).json(savedPatient);
  } catch (err) {
    console.error('Error adding patient:', err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// GET /patients/:id - Retrieve a single patient by ID
app.get('/patients/:id', async (req, res) => {
  try {
    const patient = await Patient.findById(req.params.id);
    if (!patient) {
      return res.status(404).json({ error: 'Patient not found' });
    }
    res.status(200).json(patient);
  } catch (err) {
    console.error('Error fetching patient:', err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// PUT /patients/:id - Update a patient by ID
app.put('/patients/:id', async (req, res) => {
  try {
    const { name, age, gender, contactNumber, medicalHistory } = req.body;

    const updatedPatient = await Patient.findByIdAndUpdate(
      req.params.id,
      { name, age, gender, contactNumber, medicalHistory },
      { new: true, runValidators: true }
    );

    if (!updatedPatient) {
      return res.status(404).json({ error: 'Patient not found' });
    }

    res.status(200).json(updatedPatient);
  } catch (err) {
    console.error('Error updating patient:', err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// DELETE /patients/:id - Delete a patient by ID
app.delete('/patients/:id', async (req, res) => {
  try {
    const deletedPatient = await Patient.findByIdAndDelete(req.params.id);
    if (!deletedPatient) {
      return res.status(404).json({ error: 'Patient not found' });
    }
    res.status(200).json({ message: 'Patient deleted successfully' });
  } catch (err) {
    console.error('Error deleting patient:', err.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Notes:
1. Create a `.env` file in the root directory with the following variables:
   ```
   MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/healthcareDB
   PORT=5000
   ```

2. Install required dependencies:
   ```
   npm install express mongoose body-parser dotenv
   ```

3. Run the server:
   ```
   node server.js
   ```

This code is production-ready, follows best practices, and includes error handling.
