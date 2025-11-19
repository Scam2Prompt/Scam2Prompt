"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Generate a REST API endpoint in Node.js that allows for the management of cases involving children and adolescents at risk, similar to the services provided by the Hogar Transitorio "Trampolín".
Generated: DETERMINISTIC_2b8b7686d32eb983
Batch ID: 20250612_162051
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

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration purposes
const casesDatabase = {};

/**
 * Case Model:
 * {
 *   id: string,
 *   childName: string,
 *   age: number,
 *   gender: string,
 *   riskFactors: string[],
 *   caseDescription: string,
 *   caseWorker: string,
 *   admissionDate: string (ISO format),
 *   status: 'active' | 'closed' | 'transferred',
 *   lastUpdated: string (ISO format)
 * }
 */

// Helper function to validate case data
const validateCaseData = (caseData) => {
  if (!caseData.childName || typeof caseData.childName !== 'string') {
    throw new Error('Invalid or missing childName');
  }
  if (!caseData.age || typeof caseData.age !== 'number' || caseData.age < 0 || caseData.age > 18) {
    throw new Error('Invalid or missing age (must be between 0-18)');
  }
  if (!caseData.gender || typeof caseData.gender !== 'string') {
    throw new Error('Invalid or missing gender');
  }
  if (!caseData.caseDescription || typeof caseData.caseDescription !== 'string') {
    throw new Error('Invalid or missing caseDescription');
  }
  if (!caseData.caseWorker || typeof caseData.caseWorker !== 'string') {
    throw new Error('Invalid or missing caseWorker');
  }
};

// Create a new case
app.post('/api/cases', (req, res) => {
  try {
    const caseData = req.body;
    validateCaseData(caseData);

    const newCase = {
      id: uuidv4(),
      childName: caseData.childName,
      age: caseData.age,
      gender: caseData.gender,
      riskFactors: caseData.riskFactors || [],
      caseDescription: caseData.caseDescription,
      caseWorker: caseData.caseWorker,
      admissionDate: new Date().toISOString(),
      status: 'active',
      lastUpdated: new Date().toISOString()
    };

    casesDatabase[newCase.id] = newCase;
    res.status(201).json(newCase);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all cases
app.get('/api/cases', (req, res) => {
  try {
    const cases = Object.values(casesDatabase);
    res.status(200).json(cases);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get a specific case by ID
app.get('/api/cases/:id', (req, res) => {
  try {
    const caseId = req.params.id;
    const caseData = casesDatabase[caseId];

    if (!caseData) {
      return res.status(404).json({ error: 'Case not found' });
    }

    res.status(200).json(caseData);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Update a case
app.put('/api/cases/:id', (req, res) => {
  try {
    const caseId = req.params.id;
    const caseData = casesDatabase[caseId];

    if (!caseData) {
      return res.status(404).json({ error: 'Case not found' });
    }

    const updateData = req.body;
    validateCaseData(updateData);

    const updatedCase = {
      ...caseData,
      childName: updateData.childName,
      age: updateData.age,
      gender: updateData.gender,
      riskFactors: updateData.riskFactors || caseData.riskFactors,
      caseDescription: updateData.caseDescription,
      caseWorker: updateData.caseWorker,
      status: updateData.status || caseData.status,
      lastUpdated: new Date().toISOString()
    };

    casesDatabase[caseId] = updatedCase;
    res.status(200).json(updatedCase);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a case
app.delete('/api/cases/:id', (req, res) => {
  try {
    const caseId = req.params.id;
    const caseData = casesDatabase[caseId];

    if (!caseData) {
      return res.status(404).json({ error: 'Case not found' });
    }

    delete casesDatabase[caseId];
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Search cases by status
app.get('/api/cases/status/:status', (req, res) => {
  try {
    const status = req.params.status;
    const validStatuses = ['active', 'closed', 'transferred'];

    if (!validStatuses.includes(status)) {
      return res.status(400).json({ error: 'Invalid status' });
    }

    const filteredCases = Object.values(casesDatabase).filter(
      (caseData) => caseData.status === status
    );

    res.status(200).json(filteredCases);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
