"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Create a RESTful API in Node.js to manage environmental policies and goals for an organization focused on Umweltschutz, incorporating features similar to those implied on the website.
Generated: DETERMINISTIC_b7ea0d940644c4f8
Batch ID: 20250622_204803
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory database (for demonstration purposes)
const policies = [];

// Routes

/**
 * GET /policies
 * Retrieve all environmental policies.
 */
app.get('/policies', (req, res) => {
  res.status(200).json({
    success: true,
    data: policies,
  });
});

/**
 * POST /policies
 * Create a new environmental policy.
 */
app.post('/policies', (req, res) => {
  try {
    const { title, description, goals } = req.body;

    // Validate request body
    if (!title || !description || !Array.isArray(goals)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid request. Title, description, and goals are required.',
      });
    }

    // Create a new policy
    const newPolicy = {
      id: uuidv4(),
      title,
      description,
      goals,
      createdAt: new Date(),
    };

    // Add policy to the database
    policies.push(newPolicy);

    res.status(201).json({
      success: true,
      data: newPolicy,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while creating the policy.',
    });
  }
});

/**
 * GET /policies/:id
 * Retrieve a specific environmental policy by ID.
 */
app.get('/policies/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find policy by ID
    const policy = policies.find((p) => p.id === id);

    if (!policy) {
      return res.status(404).json({
        success: false,
        message: 'Policy not found.',
      });
    }

    res.status(200).json({
      success: true,
      data: policy,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while retrieving the policy.',
    });
  }
});

/**
 * PUT /policies/:id
 * Update an existing environmental policy by ID.
 */
app.put('/policies/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { title, description, goals } = req.body;

    // Find policy by ID
    const policyIndex = policies.findIndex((p) => p.id === id);

    if (policyIndex === -1) {
      return res.status(404).json({
        success: false,
        message: 'Policy not found.',
      });
    }

    // Validate request body
    if (!title || !description || !Array.isArray(goals)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid request. Title, description, and goals are required.',
      });
    }

    // Update policy
    policies[policyIndex] = {
      ...policies[policyIndex],
      title,
      description,
      goals,
      updatedAt: new Date(),
    };

    res.status(200).json({
      success: true,
      data: policies[policyIndex],
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while updating the policy.',
    });
  }
});

/**
 * DELETE /policies/:id
 * Delete an environmental policy by ID.
 */
app.delete('/policies/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find policy by ID
    const policyIndex = policies.findIndex((p) => p.id === id);

    if (policyIndex === -1) {
      return res.status(404).json({
        success: false,
        message: 'Policy not found.',
      });
    }

    // Remove policy from the database
    const deletedPolicy = policies.splice(policyIndex, 1);

    res.status(200).json({
      success: true,
      data: deletedPolicy[0],
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while deleting the policy.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
