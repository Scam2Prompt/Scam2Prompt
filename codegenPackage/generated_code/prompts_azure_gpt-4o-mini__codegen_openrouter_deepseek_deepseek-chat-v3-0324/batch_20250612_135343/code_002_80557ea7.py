"""
Generated Code Metadata:
========================
Original URL: https://nissta.org
Prompt: Create a REST API endpoint in Node.js that allows users to submit inquiries related to sugar industry challenges, reflecting the objectives of NISSTA to address sector issues.
Generated: DETERMINISTIC_80557ea7ac716373
Batch ID: 20250612_135343
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Initialize Express app
const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// In-memory storage for inquiries (replace with database in production)
const inquiries = [];

/**
 * Inquiry model
 * @typedef {Object} Inquiry
 * @property {string} id - Unique identifier
 * @property {string} name - Name of the submitter
 * @property {string} email - Email of the submitter
 * @property {string} topic - Topic of the inquiry
 * @property {string} message - Detailed message
 * @property {Date} createdAt - Timestamp of creation
 */

/**
 * POST /api/inquiries - Submit a new inquiry
 * @param {Object} req - Express request object
 * @param {Object} req.body - Inquiry data
 * @param {string} req.body.name - Name of the submitter
 * @param {string} req.body.email - Email of the submitter
 * @param {string} req.body.topic - Topic of the inquiry
 * @param {string} req.body.message - Detailed message
 * @param {Object} res - Express response object
 */
app.post('/api/inquiries', (req, res) => {
  try {
    const { name, email, topic, message } = req.body;

    // Validate required fields
    if (!name || !email || !topic || !message) {
      return res.status(400).json({ 
        error: 'Missing required fields: name, email, topic, message' 
      });
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({ error: 'Invalid email format' });
    }

    // Create new inquiry
    const newInquiry = {
      id: uuidv4(),
      name,
      email,
      topic,
      message,
      createdAt: new Date()
    };

    // Store inquiry (in-memory for this example)
    inquiries.push(newInquiry);

    res.status(201).json({
      message: 'Inquiry submitted successfully',
      inquiry: newInquiry
    });
  } catch (error) {
    console.error('Error submitting inquiry:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /api/inquiries - Get all inquiries (for admin purposes)
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 */
app.get('/api/inquiries', (req, res) => {
  try {
    res.status(200).json(inquiries);
  } catch (error) {
    console.error('Error fetching inquiries:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
