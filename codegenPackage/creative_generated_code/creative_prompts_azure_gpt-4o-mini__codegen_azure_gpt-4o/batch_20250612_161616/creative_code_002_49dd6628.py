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
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express app
const app = express();
const PORT = 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory database simulation (for demonstration purposes)
// Normally, you would use a real database like MongoDB or PostgreSQL
const patientRecords = {};

// Helper function to validate patient data
const validatePatientData = (data) => {
  const { name, age, healthCheckups, labTests } = data;
  if (!name || typeof name !== 'string') return 'Invalid name';
  if (!age || typeof age !== 'number') return 'Invalid age';
  if (!Array.isArray(healthCheckups)) return 'Invalid healthCheckups';
  if (!Array.isArray(labTests)) return 'Invalid labTests';
  return null;
};

// REST API Endpoints

// Create a new patient record
app.post('/patients', (req, res) => {
  const validationError = validatePatientData(req.body);
  if (validationError) {
    return res.status(400).json({ error: validationError });
  }

  const newPatient = {
    id: uuidv4(),
    ...req.body,
  };

  patientRecords[newPatient.id] = newPatient;
  res.status(201).json(newPatient);
});

// Get all patient records
app.get('/patients', (req, res) => {
  res.status(200).json(Object.values(patientRecords));
});

// Get a specific patient record by ID
app.get('/patients/:id', (req, res) => {
  const patient = patientRecords[req.params.id];
  if (!patient) {
    return res.status(404).json({ error: 'Patient not found' });
  }
  res.status(200).json(patient);
});

// Update a specific patient record by ID
app.put('/patients/:id', (req, res) => {
  const patient = patientRecords[req.params.id];
  if (!patient) {
    return res.status(404).json({ error: 'Patient not found' });
  }

  const validationError = validatePatientData(req.body);
  if (validationError) {
    return res.status(400).json({ error: validationError });
  }

  patientRecords[req.params.id] = {
    id: req.params.id, // Keep the ID unchanged
    ...req.body,
  };

  res.status(200).json(patientRecords[req.params.id]);
});

// Delete a specific patient record by ID
app.delete('/patients/:id', (req, res) => {
  const patient = patientRecords[req.params.id];
  if (!patient) {
    return res.status(404).json({ error: 'Patient not found' });
  }

  delete patientRecords[req.params.id];
  res.status(204).send(); // No content
});

// Error handling middleware (for unexpected server errors)
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
