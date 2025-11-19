"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.net
Prompt: Develop a REST API endpoint in Node.js that mimics the data structure of medical evaluations as seen in the offerings of Medizinische Gutachteninstitut Döbeln.
Generated: DETERMINISTIC_5cd137f1f0d449ce
Batch ID: 20250612_163817
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

// Initialize Express app
const app = express();

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// Data structure for medical evaluations
// This structure mimics what could be offered by a medical institute
const medicalEvaluations = [
  {
    id: 1,
    patientName: "John Doe",
    dateOfEvaluation: "2023-10-01",
    evaluationType: "Orthopedic Assessment",
    findings: {
      diagnosis: "Knee Osteoarthritis",
      recommendations: "Physical Therapy, Pain Management",
    },
    physician: {
      name: "Dr. Maria Smith",
      specialty: "Orthopedics",
    },
  },
  {
    id: 2,
    patientName: "Jane Roe",
    dateOfEvaluation: "2023-09-20",
    evaluationType: "Neurological Assessment",
    findings: {
      diagnosis: "Migraine",
      recommendations: "Avoid triggers, Regular exercise",
    },
    physician: {
      name: "Dr. Henry Brown",
      specialty: "Neurology",
    },
  },
];

// GET endpoint to retrieve all medical evaluations
app.get('/api/medical-evaluations', (req, res) => {
  try {
    // Return the full list of evaluations
    res.status(200).json({
      success: true,
      data: medicalEvaluations,
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while retrieving medical evaluations.',
      error: error.message,
    });
  }
});

// GET endpoint to retrieve a specific medical evaluation by ID
app.get('/api/medical-evaluations/:id', (req, res) => {
  try {
    const { id } = req.params;
    const evaluation = medicalEvaluations.find((e) => e.id === parseInt(id));

    if (!evaluation) {
      // Return 404 if evaluation is not found
      return res.status(404).json({
        success: false,
        message: 'Medical evaluation not found.',
      });
    }

    // Return the evaluation if found
    res.status(200).json({
      success: true,
      data: evaluation,
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while retrieving the medical evaluation.',
      error: error.message,
    });
  }
});

// POST endpoint to create a new medical evaluation
app.post('/api/medical-evaluations', (req, res) => {
  try {
    const { patientName, dateOfEvaluation, evaluationType, findings, physician } = req.body;

    // Validate required fields
    if (!patientName || !dateOfEvaluation || !evaluationType || !findings || !physician) {
      return res.status(400).json({
        success: false,
        message: 'Missing required fields.',
      });
    }

    // Create new evaluation object
    const newEvaluation = {
      id: medicalEvaluations.length + 1, // Auto-incrementing ID
      patientName,
      dateOfEvaluation,
      evaluationType,
      findings,
      physician,
    };

    // Add the new evaluation to the list
    medicalEvaluations.push(newEvaluation);

    // Return the newly created evaluation
    res.status(201).json({
      success: true,
      data: newEvaluation,
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while creating the medical evaluation.',
      error: error.message,
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
