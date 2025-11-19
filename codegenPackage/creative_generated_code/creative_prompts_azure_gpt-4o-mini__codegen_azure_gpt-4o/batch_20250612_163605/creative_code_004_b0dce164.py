"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aamctg.edu.bd
Prompt: Construct a REST API endpoint in Node.js to manage student registration for the Alim examination at Ashekane Aulia Fazil Madrasah.
Generated: DETERMINISTIC_b0dce16418e3c7c8
Batch ID: 20250612_163605
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

// Initialize the app
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// In-memory database (replace with a real database in production)
let students = [];

// Endpoint to register a student for the Alim examination
/**
 * POST /api/register
 * Registers a student for the Alim examination.
 * Request Body:
 *  {
 *    "name": "Student Name",
 *    "age": 18,
 *    "email": "student@example.com",
 *    "phone": "1234567890"
 *  }
 * Response:
 *  {
 *    "success": true,
 *    "message": "Student registered successfully.",
 *    "studentId": "generated-uuid"
 *  }
 */
app.post('/api/register', (req, res) => {
  try {
    const { name, age, email, phone } = req.body;

    // Validate input
    if (!name || typeof name !== 'string' || name.trim() === '') {
      return res.status(400).json({ success: false, message: 'Invalid name provided.' });
    }
    if (!age || typeof age !== 'number' || age < 0) {
      return res.status(400).json({ success: false, message: 'Invalid age provided.' });
    }
    if (!email || typeof email !== 'string' || !email.includes('@')) {
      return res.status(400).json({ success: false, message: 'Invalid email address provided.' });
    }
    if (!phone || typeof phone !== 'string' || phone.length !== 10) {
      return res.status(400).json({ success: false, message: 'Invalid phone number provided.' });
    }

    // Create a new student record
    const newStudent = {
      id: uuidv4(), // Generate a unique ID for the student
      name: name.trim(),
      age,
      email: email.trim(),
      phone: phone.trim(),
      registrationDate: new Date().toISOString(),
    };

    // Store the student record in the in-memory database
    students.push(newStudent);

    // Respond with success
    res.status(201).json({
      success: true,
      message: 'Student registered successfully.',
      studentId: newStudent.id,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while registering student:', error);
    res.status(500).json({
      success: false,
      message: 'An unexpected error occurred.',
    });
  }
});

// Endpoint to retrieve all registered students
/**
 * GET /api/students
 * Retrieves a list of all students registered for the Alim examination.
 * Response:
 *  [
 *    {
 *      "id": "generated-uuid",
 *      "name": "Student Name",
 *      "age": 18,
 *      "email": "student@example.com",
 *      "phone": "1234567890",
 *      "registrationDate": "2023-01-01T00:00:00.000Z"
 *    }
 *  ]
 */
app.get('/api/students', (req, res) => {
  try {
    res.status(200).json(students);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while retrieving students:', error);
    res.status(500).json({
      success: false,
      message: 'An unexpected error occurred.',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
