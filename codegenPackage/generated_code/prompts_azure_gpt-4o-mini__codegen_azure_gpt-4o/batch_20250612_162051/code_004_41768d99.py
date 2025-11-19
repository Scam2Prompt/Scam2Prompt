"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: Construct a RESTful API endpoint in Node.js that allows users to enroll in the Corsi di formazione offered by Geta Consulenze, including error handling for course availability.
Generated: DETERMINISTIC_41768d997afcabeb
Batch ID: 20250612_162051
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

// Initialize the Express application
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON request bodies

// Mock database for courses and enrollments
const courses = [
  { id: 1, name: 'Course A', availableSlots: 5 },
  { id: 2, name: 'Course B', availableSlots: 0 },
  { id: 3, name: 'Course C', availableSlots: 10 },
];

const enrollments = [];

// Endpoint to enroll in a course
app.post('/api/enroll', (req, res) => {
  try {
    // Extract courseId and userId from the request body
    const { courseId, userId } = req.body;

    // Validate input
    if (!courseId || !userId) {
      return res.status(400).json({ error: 'courseId and userId are required.' });
    }

    // Find the course by ID
    const course = courses.find((c) => c.id === courseId);

    // Check if the course exists
    if (!course) {
      return res.status(404).json({ error: 'Course not found.' });
    }

    // Check if the course has available slots
    if (course.availableSlots <= 0) {
      return res.status(400).json({ error: 'No available slots for this course.' });
    }

    // Enroll the user in the course
    enrollments.push({ userId, courseId });
    course.availableSlots -= 1; // Decrease available slots

    // Respond with success
    return res.status(200).json({
      message: 'Enrollment successful.',
      enrollment: { userId, courseId },
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error during enrollment:', error);
    return res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
