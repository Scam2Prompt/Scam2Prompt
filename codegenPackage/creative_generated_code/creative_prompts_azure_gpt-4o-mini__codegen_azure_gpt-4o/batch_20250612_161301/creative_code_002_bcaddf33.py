"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Create a REST API endpoint in Node.js that allows users to submit applications for courses at the Kigali Institute, emphasizing the scholarship and financial aid options.
Generated: DETERMINISTIC_bcaddf33df01dca0
Batch ID: 20250612_161301
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

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON
app.use(bodyParser.json());

// Dummy database for storing applications
const applications = [];

/**
 * POST /api/applications
 * Endpoint for submitting course applications
 * @requestBody {object} - JSON payload containing application details
 *  {
 *    "fullName": "John Doe",
 *    "email": "john.doe@example.com",
 *    "phone": "+250789123456",
 *    "course": "Computer Science",
 *    "scholarshipInterest": true,
 *    "financialAidInterest": false
 *  }
 * @response {object} - Confirmation of application submission
 */
app.post('/api/applications', (req, res) => {
  try {
    // Validate input
    const { fullName, email, phone, course, scholarshipInterest, financialAidInterest } = req.body;

    if (!fullName || !email || !phone || !course) {
      return res.status(400).json({
        error: 'Missing required fields: fullName, email, phone, course',
      });
    }

    // Create application object
    const application = {
      id: uuidv4(), // Unique application ID
      fullName,
      email,
      phone,
      course,
      scholarshipInterest: scholarshipInterest || false,
      financialAidInterest: financialAidInterest || false,
      submittedAt: new Date().toISOString(), // Timestamp
    };

    // Store the application in the dummy database
    applications.push(application);

    // Respond with success message
    res.status(201).json({
      message: 'Application successfully submitted',
      application,
    });
  } catch (error) {
    // Error handling
    console.error('Error submitting application:', error.message);
    res.status(500).json({
      error: 'An internal server error occurred',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
