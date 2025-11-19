"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a REST API endpoint in Node.js that allows users to submit academic requests to I.E Politécnico Municipal Cali, ensuring it handles responses for various types of inquiries.
Generated: DETERMINISTIC_a7a7b7e00ac0dd06
Batch ID: 20250612_161301
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
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Define a class for AcademicRequest
class AcademicRequest {
  /**
   * Constructor for AcademicRequest
   * @param {string} studentName 
   * @param {string} studentId 
   * @param {string} inquiryType 
   * @param {string} description 
   */
  constructor(studentName, studentId, inquiryType, description) {
    this.studentName = studentName;
    this.studentId = studentId;
    this.inquiryType = inquiryType;
    this.description = description;
  }
}

// In-memory storage for academic requests (replace with a database in production)
let academicRequests = [];

// Define API endpoint to submit academic requests
app.post('/api/academic-requests', (req, res) => {
  try {
    // Validate request body
    if (!req.body.studentName || !req.body.studentId || !req.body.inquiryType || !req.body.description) {
      res.status(400).send({ message: 'Please provide all required fields' });
      return;
    }

    // Create a new AcademicRequest instance
    const request = new AcademicRequest(
      req.body.studentName,
      req.body.studentId,
      req.body.inquiryType,
      req.body.description
    );

    // Store the request
    academicRequests.push(request);

    // Return a success response
    res.status(201).send({ message: 'Academic request submitted successfully' });
  } catch (error) {
    // Handle internal server errors
    console.error(error);
    res.status(500).send({ message: 'Internal server error' });
  }
});

// Define API endpoint to retrieve all academic requests
app.get('/api/academic-requests', (req, res) => {
  try {
    // Return all academic requests
    res.status(200).send(academicRequests);
  } catch (error) {
    // Handle internal server errors
    console.error(error);
    res.status(500).send({ message: 'Internal server error' });
  }
});

// Define API endpoint to retrieve academic requests by inquiry type
app.get('/api/academic-requests/:inquiryType', (req, res) => {
  try {
    // Filter academic requests by inquiry type
    const inquiryType = req.params.inquiryType;
    const requests = academicRequests.filter(request => request.inquiryType === inquiryType);

    // Return filtered academic requests
    res.status(200).send(requests);
  } catch (error) {
    // Handle internal server errors
    console.error(error);
    res.status(500).send({ message: 'Internal server error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Handle server errors
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});
```
