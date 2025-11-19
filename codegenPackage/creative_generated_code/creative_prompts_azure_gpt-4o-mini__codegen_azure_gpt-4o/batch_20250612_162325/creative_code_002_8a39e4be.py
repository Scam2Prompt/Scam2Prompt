"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tidhholding.com
Prompt: Create a RESTful API endpoint using Node.js that allows users to submit project proposals to TIDH Holding for potential investment collaboration.
Generated: DETERMINISTIC_8a39e4bebacd25d9
Batch ID: 20250612_162325
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
const { body, validationResult } = require('express-validator'); // Input validation
const uuid = require('uuid'); // Unique ID generation

// Initialize the Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory database for storing project proposals (Replace with real database in production)
const proposals = [];

// POST endpoint for submitting project proposals
app.post(
  '/api/proposals',
  [
    // Validate input fields
    body('name').isString().notEmpty().withMessage('Name is required and must be a string.'),
    body('email').isEmail().withMessage('Valid email is required.'),
    body('projectTitle').isString().notEmpty().withMessage('Project title is required and must be a string.'),
    body('description').isString().notEmpty().withMessage('Project description is required.'),
    body('estimatedBudget')
      .isFloat({ min: 0 })
      .notEmpty()
      .withMessage('Estimated budget is required and must be a positive number.'),
  ],
  (req, res) => {
    // Handle validation errors
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      // Extract proposal data from the request body
      const { name, email, projectTitle, description, estimatedBudget } = req.body;

      // Generate a unique ID for the proposal
      const proposalId = uuid.v4();

      // Create a new proposal object
      const newProposal = {
        id: proposalId,
        name,
        email,
        projectTitle,
        description,
        estimatedBudget,
        submittedAt: new Date(),
      };

      // Store the proposal (In production, save to the database)
      proposals.push(newProposal);

      // Respond with success
      res.status(201).json({
        message: 'Proposal submitted successfully.',
        proposal: newProposal,
      });
    } catch (error) {
      // Handle unexpected errors
      console.error('Error while processing the proposal submission:', error);
      res.status(500).json({
        message: 'An unexpected error occurred while submitting your proposal.',
      });
    }
  }
);

// Start the server
const PORT = process.env.PORT || 3000; // Port configuration
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing purposes (optional in production-ready code)
module.exports = app;
```
