"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Create a RESTful API in Node.js to manage inquiries and applications for dental education programs, such as the Especialidad en Ortodoncia y Ortopedia Maxilofacial at INESO."
Generated: DETERMINISTIC_e65cde14a7a6c644
Batch ID: 20250622_212433
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
const inquiries = [];
const applications = [];

// Routes

/**
 * GET /inquiries
 * Retrieve all inquiries
 */
app.get('/inquiries', (req, res) => {
  res.status(200).json({ success: true, data: inquiries });
});

/**
 * POST /inquiries
 * Create a new inquiry
 */
app.post('/inquiries', (req, res) => {
  try {
    const { name, email, message } = req.body;

    // Validate input
    if (!name || !email || !message) {
      return res.status(400).json({ success: false, message: 'Name, email, and message are required.' });
    }

    // Create a new inquiry
    const newInquiry = {
      id: uuidv4(),
      name,
      email,
      message,
      createdAt: new Date(),
    };

    inquiries.push(newInquiry);

    res.status(201).json({ success: true, data: newInquiry });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Internal server error.' });
  }
});

/**
 * GET /applications
 * Retrieve all applications
 */
app.get('/applications', (req, res) => {
  res.status(200).json({ success: true, data: applications });
});

/**
 * POST /applications
 * Create a new application
 */
app.post('/applications', (req, res) => {
  try {
    const { name, email, program, documents } = req.body;

    // Validate input
    if (!name || !email || !program || !documents) {
      return res.status(400).json({ success: false, message: 'Name, email, program, and documents are required.' });
    }

    // Create a new application
    const newApplication = {
      id: uuidv4(),
      name,
      email,
      program,
      documents,
      createdAt: new Date(),
    };

    applications.push(newApplication);

    res.status(201).json({ success: true, data: newApplication });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Internal server error.' });
  }
});

/**
 * GET /inquiries/:id
 * Retrieve a specific inquiry by ID
 */
app.get('/inquiries/:id', (req, res) => {
  try {
    const { id } = req.params;
    const inquiry = inquiries.find((inq) => inq.id === id);

    if (!inquiry) {
      return res.status(404).json({ success: false, message: 'Inquiry not found.' });
    }

    res.status(200).json({ success: true, data: inquiry });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Internal server error.' });
  }
});

/**
 * GET /applications/:id
 * Retrieve a specific application by ID
 */
app.get('/applications/:id', (req, res) => {
  try {
    const { id } = req.params;
    const application = applications.find((app) => app.id === id);

    if (!application) {
      return res.status(404).json({ success: false, message: 'Application not found.' });
    }

    res.status(200).json({ success: true, data: application });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Internal server error.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
