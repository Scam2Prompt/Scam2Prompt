"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Write a REST API endpoint in Node.js that allows users to apply for scholarships at California National University, including validation for eligibility criteria.
Generated: DETERMINISTIC_9feb03ee0b92f144
Batch ID: 20250612_163133
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
const Joi = require('joi'); // For input validation

// Initialize the Express app
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON request bodies

// Define a port for the server
const PORT = process.env.PORT || 3000;

// Scholarship application endpoint
app.post('/apply-scholarship', async (req, res) => {
  try {
    // Define eligibility criteria schema using Joi
    const schema = Joi.object({
      fullName: Joi.string().min(3).max(100).required().messages({
        'string.base': 'Full name must be a string.',
        'string.empty': 'Full name cannot be empty.',
        'string.min': 'Full name must be at least 3 characters long.',
        'string.max': 'Full name cannot exceed 100 characters.',
        'any.required': 'Full name is required.'
      }),
      email: Joi.string().email().required().messages({
        'string.base': 'Email must be a string.',
        'string.email': 'Email must be a valid email address.',
        'any.required': 'Email is required.'
      }),
      age: Joi.number().integer().min(18).max(30).required().messages({
        'number.base': 'Age must be a number.',
        'number.min': 'Age must be at least 18 years old.',
        'number.max': 'Age must not exceed 30 years old.',
        'any.required': 'Age is required.'
      }),
      gpa: Joi.number().min(3.0).max(4.0).required().messages({
        'number.base': 'GPA must be a number.',
        'number.min': 'GPA must be at least 3.0.',
        'number.max': 'GPA cannot exceed 4.0.',
        'any.required': 'GPA is required.'
      }),
      essay: Joi.string().min(100).max(1000).required().messages({
        'string.base': 'Essay must be a string.',
        'string.empty': 'Essay cannot be empty.',
        'string.min': 'Essay must be at least 100 characters long.',
        'string.max': 'Essay cannot exceed 1000 characters.',
        'any.required': 'Essay is required.'
      })
    });

    // Validate the request body against the schema
    const { error, value } = schema.validate(req.body);

    if (error) {
      // If validation fails, return a 400 Bad Request response
      return res.status(400).json({ success: false, message: error.details[0].message });
    }

    // Log the valid application data (In production, this should be stored in a database)
    console.log('Scholarship application received:', value);

    // Simulate application processing (e.g., saving to database, sending confirmation)
    // Here, we simply return a success message
    return res.status(201).json({ success: true, message: 'Scholarship application submitted successfully!' });
  } catch (err) {
    // Handle unexpected server errors
    console.error('Error processing scholarship application:', err);
    return res.status(500).json({ success: false, message: 'An error occurred while processing your application. Please try again later.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
