"""
Generated Code Metadata:
========================
Original URL: https://deviationinfotech.in
Prompt: "Design a web development project using React, Node.js, and MongoDB for a client in the healthcare industry, based on Deviation Infotech's web design and development services."
Generated: DETERMINISTIC_f41e16ff3e66c709
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is the code for a simple web development project using React, Node.js, and MongoDB for a healthcare client. It includes a basic patient management system with CRUD functionality.

---

### Backend: Node.js + Express + MongoDB

#### `server.js`
```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(express.json());
app.use(cors());

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => console.log('MongoDB connected'))
  .catch((err) => console.error('MongoDB connection error:', err));

// Define Patient schema and model
const patientSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
  gender: { type: String, required: true },
  contact: { type: String, required: true },
  medicalHistory: { type: String },
}, { timestamps: true });

const Patient = mongoose.model('Patient', patientSchema);

// Routes
// Get all patients
app.get('/api/patients', async (req, res) => {
  try {
    const patients = await Patient.find();
    res.status(200).json(patients);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch patients' });
  }
});

// Get a single patient by ID
app.get('/api/patients/:id', async (req, res) => {
  try {
    const patient = await Patient.findById(req.params.id);
    if (!patient) return res.status(404).json({ error: 'Patient not found' });
    res.status(200).json(patient);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch patient' });
  }
});

// Create a new patient
app.post('/api/patients', async (req, res) => {
  try {
    const newPatient = new Patient(req.body);
    const savedPatient = await newPatient.save();
    res.status(201).json(savedPatient);
  } catch (err) {
    res.status(400).json({ error: 'Failed to create patient' });
  }
});

// Update a patient
app.put('/api/patients/:id', async (req, res) => {
  try {
    const updatedPatient = await Patient.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!updatedPatient) return res.status(404).json({ error: 'Patient not found' });
    res.status(200).json(updatedPatient);
  } catch (err) {
    res.status(400).json({ error: 'Failed to update patient' });
  }
});

// Delete a patient
app.delete('/api/patients/:id', async (req, res) => {
  try {
    const deletedPatient = await Patient.findByIdAndDelete(req.params.id);
    if (!deletedPatient) return res.status(404).json({ error: 'Patient not found' });
    res.status(200).json({ message: 'Patient deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete patient' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

### Frontend: React

#### `src/App.js`
```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [patients, setPatients] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    gender: '',
    contact: '',
    medicalHistory: '',
  });

  // Fetch patients from the backend
  useEffect(() => {
    const fetchPatients = async () => {
      try {
        const response = await axios.get('/api/patients');
        setPatients(response.data);
      } catch (err) {
        console.error('Error fetching patients:', err);
      }
    };
    fetchPatients();
  }, []);

  // Handle form input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/patients', formData);
      setPatients([...patients, response.data]);
      setFormData({
        name: '',
        age: '',
        gender: '',
        contact: '',
        medicalHistory: '',
      });
    } catch (err) {
      console.error('Error adding patient:', err);
    }
  };

  return (
    <div>
      <h1>Healthcare Patient Management</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="age"
          placeholder="Age"
          value={formData.age}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="gender"
          placeholder="Gender"
          value={formData.gender}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="contact"
          placeholder="Contact"
          value={formData.contact}
          onChange={handleChange}
          required
        />
        <textarea
          name="medicalHistory"
          placeholder="Medical History"
          value={formData.medicalHistory}
          onChange={handleChange}
        />
        <button type="submit">Add Patient</button>
      </form>
      <h2>Patient List</h2>
      <ul>
        {patients.map((patient) => (
          <li key={patient._id}>
            {patient.name} - {patient.age} - {patient.gender} - {patient.contact}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
```

---

### Environment Variables

#### `.env`
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/healthcareDB
PORT=5000
```

---

### Notes:
1. Install dependencies:
   - Backend: `npm install express mongoose cors dotenv`
   - Frontend: `npm install axios`
2. Run the backend server: `node server.js`
3. Run the React frontend: `npm start` in the React project directory.
4. Ensure MongoDB is running and replace `<username>` and `<password>` in `.env` with your credentials.
