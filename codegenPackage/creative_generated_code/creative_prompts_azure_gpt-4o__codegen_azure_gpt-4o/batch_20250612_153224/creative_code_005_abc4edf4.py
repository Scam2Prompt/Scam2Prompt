"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stockyardrefacing.com
Prompt: Develop a REST API in Node.js to manage customer inquiries for cabinet refacing services. Include endpoints for submitting inquiries, retrieving project details, and scheduling consultations.
Generated: DETERMINISTIC_abc4edf41561bf89
Batch ID: 20250612_153224
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

// Middleware setup
app.use(bodyParser.json());

// Simulated in-memory database for customer inquiries
const inquiries = {};

// Route: Submit a new inquiry
app.post('/api/inquiries', (req, res) => {
  try {
    const { name, email, phone, projectDetails } = req.body;

    // Validate input
    if (!name || !email || !projectDetails) {
      return res.status(400).json({ error: 'Name, email, and project details are required.' });
    }

    // Create a new inquiry object
    const inquiryId = uuidv4();
    inquiries[inquiryId] = {
      id: inquiryId,
      name,
      email,
      phone: phone || null, // Optional field
      projectDetails,
      consultationScheduled: false,
    };

    res.status(201).json({ message: 'Inquiry submitted successfully.', inquiryId });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while submitting the inquiry.' });
  }
});

// Route: Retrieve details of an inquiry by ID
app.get('/api/inquiries/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Check if the inquiry exists
    const inquiry = inquiries[id];
    if (!inquiry) {
      return res.status(404).json({ error: 'Inquiry not found.' });
    }

    res.status(200).json({ inquiry });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while retrieving the inquiry.' });
  }
});

// Route: Schedule a consultation for an inquiry
app.post('/api/inquiries/:id/schedule-consultation', (req, res) => {
  try {
    const { id } = req.params;

    // Check if the inquiry exists
    const inquiry = inquiries[id];
    if (!inquiry) {
      return res.status(404).json({ error: 'Inquiry not found.' });
    }

    // Update inquiry to mark consultation as scheduled
    inquiry.consultationScheduled = true;

    res.status(200).json({ message: 'Consultation scheduled successfully.', inquiry });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while scheduling the consultation.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
