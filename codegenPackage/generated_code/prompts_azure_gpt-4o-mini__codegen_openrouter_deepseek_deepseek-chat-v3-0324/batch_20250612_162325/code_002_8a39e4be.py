"""
Generated Code Metadata:
========================
Original URL: https://tidhholding.com
Prompt: Create a RESTful API endpoint using Node.js that allows users to submit project proposals to TIDH Holding for potential investment collaboration.
Generated: DETERMINISTIC_8a39e4bebacd25d9
Batch ID: 20250612_162325
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
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');
const Joi = require('joi');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database (replace with actual database in production)
const proposalsDB = [];

// Joi schema for proposal validation
const proposalSchema = Joi.object({
  projectName: Joi.string().required().min(3).max(100),
  description: Joi.string().required().min(10).max(1000),
  contactEmail: Joi.string().email().required(),
  estimatedBudget: Joi.number().positive().required(),
  durationMonths: Joi.number().integer().min(1).max(60).required(),
  teamMembers: Joi.array().items(Joi.string().min(2)).min(1).required(),
  businessModel: Joi.string().valid('B2B', 'B2C', 'B2G', 'Other').required(),
  marketPotential: Joi.string().required().min(10).max(500)
});

// POST endpoint for submitting proposals
app.post('/api/proposals', async (req, res) => {
  try {
    // Validate request body
    const { error, value } = proposalSchema.validate(req.body);
    if (error) {
      return res.status(400).json({ error: error.details[0].message });
    }

    // Create proposal object
    const proposal = {
      id: uuidv4(),
      ...value,
      submissionDate: new Date().toISOString(),
      status: 'Under Review'
    };

    // Store proposal (in-memory for this example)
    proposalsDB.push(proposal);

    // Return success response
    res.status(201).json({
      message: 'Proposal submitted successfully',
      proposalId: proposal.id
    });
  } catch (err) {
    console.error('Error submitting proposal:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET endpoint to retrieve all proposals (for internal use)
app.get('/api/proposals', (req, res) => {
  try {
    res.status(200).json(proposalsDB);
  } catch (err) {
    console.error('Error retrieving proposals:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET endpoint to retrieve a specific proposal
app.get('/api/proposals/:id', (req, res) => {
  try {
    const proposal = proposalsDB.find(p => p.id === req.params.id);
    if (!proposal) {
      return res.status(404).json({ error: 'Proposal not found' });
    }
    res.status(200).json(proposal);
  } catch (err) {
    console.error('Error retrieving proposal:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
