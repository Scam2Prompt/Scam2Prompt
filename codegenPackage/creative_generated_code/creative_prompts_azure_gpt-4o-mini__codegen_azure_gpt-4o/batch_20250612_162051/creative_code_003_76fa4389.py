"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Develop a REST API endpoint in Node.js that allows users to submit inquiries about properties listed on the Corfu Coastal Collection website.
Generated: DETERMINISTIC_76fa43891a4f278c
Batch ID: 20250612_162051
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
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs
const fs = require('fs');

// Initialize the Express app
const app = express();

// Middleware
app.use(bodyParser.json()); // Parse JSON request bodies

// Define the port for the server
const PORT = process.env.PORT || 3000;

// Mock database file (for simplicity, using a JSON file)
const inquiriesDatabase = 'inquiries.json';

// Ensure the database file exists
if (!fs.existsSync(inquiriesDatabase)) {
  fs.writeFileSync(inquiriesDatabase, JSON.stringify([]));
}

// POST endpoint to submit property inquiries
app.post('/api/inquiries', async (req, res) => {
  try {
    // Extract data from request body
    const { name, email, propertyId, message } = req.body;

    // Validate required fields
    if (!name || !email || !propertyId || !message) {
      return res.status(400).json({
        success: false,
        message: 'Missing required fields: name, email, propertyId, and message are required.',
      });
    }

    // Create a new inquiry object
    const newInquiry = {
      id: uuidv4(), // Generate unique ID for the inquiry
      name,
      email,
      propertyId,
      message,
      submittedAt: new Date().toISOString(),
    };

    // Read existing inquiries from database
    const inquiries = JSON.parse(fs.readFileSync(inquiriesDatabase, 'utf-8'));

    // Add new inquiry to database
    inquiries.push(newInquiry);

    // Write updated inquiries back to the database file
    fs.writeFileSync(inquiriesDatabase, JSON.stringify(inquiries, null, 2));

    // Respond with success message
    res.status(201).json({
      success: true,
      message: 'Inquiry submitted successfully.',
      inquiry: newInquiry,
    });
  } catch (error) {
    // Handle server error
    console.error('Error processing inquiry:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while processing your inquiry. Please try again later.',
    });
  }
});

// Catch all for unknown routes
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Endpoint not found.',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

```
