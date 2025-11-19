"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Generate a REST API endpoint in Node.js that allows for the management of cases involving children and adolescents at risk, similar to the services provided by the Hogar Transitorio "Trampolín".
Generated: DETERMINISTIC_2b8b7686d32eb983
Batch ID: 20250612_162051
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// In-memory database for demonstration purposes (replace with a real database in production)
let cases = [];

/**
 * @route   GET /cases
 * @desc    Retrieve all cases
 * @access  Public
 */
app.get('/cases', (req, res) => {
  res.status(200).json(cases);
});

/**
 * @route   GET /cases/:id
 * @desc    Retrieve a case by ID
 * @access  Public
 */
app.get('/cases/:id', (req, res) => {
  const caseId = req.params.id;
  const foundCase = cases.find((c) => c.id === caseId);

  if (!foundCase) {
    return res.status(404).json({ error: 'Case not found' });
  }

  res.status(200).json(foundCase);
});

/**
 * @route   POST /cases
 * @desc    Create a new case
 * @access  Public
 */
app.post('/cases', (req, res) => {
  try {
    const { name, age, riskLevel, description } = req.body;

    // Basic input validation
    if (!name || !age || !riskLevel || !description) {
      return res.status(400).json({ error: 'All fields are required: name, age, riskLevel, description' });
    }

    const newCase = {
      id: uuidv4(), // Generate a unique ID for the case
      name,
      age,
      riskLevel,
      description,
      createdAt: new Date(),
    };

    cases.push(newCase);
    res.status(201).json(newCase);
  } catch (error) {
    console.error('Error creating case:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route   PUT /cases/:id
 * @desc    Update an existing case
 * @access  Public
 */
app.put('/cases/:id', (req, res) => {
  const caseId = req.params.id;
  const { name, age, riskLevel, description } = req.body;

  const foundCase = cases.find((c) => c.id === caseId);

  if (!foundCase) {
    return res.status(404).json({ error: 'Case not found' });
  }

  // Update case details
  foundCase.name = name || foundCase.name;
  foundCase.age = age || foundCase.age;
  foundCase.riskLevel = riskLevel || foundCase.riskLevel;
  foundCase.description = description || foundCase.description;
  foundCase.updatedAt = new Date();

  res.status(200).json(foundCase);
});

/**
 * @route   DELETE /cases/:id
 * @desc    Delete a case by ID
 * @access  Public
 */
app.delete('/cases/:id', (req, res) => {
  const caseId = req.params.id;
  const index = cases.findIndex((c) => c.id === caseId);

  if (index === -1) {
    return res.status(404).json({ error: 'Case not found' });
  }

  cases.splice(index, 1);
  res.status(200).json({ message: 'Case deleted successfully' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
