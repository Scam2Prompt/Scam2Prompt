"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.getaconsulenze.it
Prompt: Construct a RESTful API endpoint in Node.js that allows users to enroll in the Corsi di formazione offered by Geta Consulenze, including error handling for course availability.
Generated: DETERMINISTIC_41768d997afcabeb
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique enrollment IDs

// Initialize the Express application
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Dummy data for courses (in a real application, this data would come from a database)
let courses = [
    { id: '1', name: 'Business Strategy', availableSlots: 5 },
    { id: '2', name: 'Digital Marketing', availableSlots: 0 },
    { id: '3', name: 'Project Management', availableSlots: 3 }
];

// Dummy data structure to hold enrollments
let enrollments = [];

// RESTful API endpoint for enrolling in a course
app.post('/api/enroll', (req, res) => {
    const { courseId, userName } = req.body;

    // Validate request payload
    if (!courseId || !userName) {
        return res.status(400).json({
            error: 'Bad Request',
            message: 'Both courseId and userName are required'
        });
    }

    // Find the course by ID
    const course = courses.find(c => c.id === courseId);

    if (!course) {
        // Return a 404 error if the course does not exist
        return res.status(404).json({
            error: 'Not Found',
            message: 'The requested course does not exist'
        });
    }

    // Check if there are available slots in the course
    if (course.availableSlots <= 0) {
        return res.status(400).json({
            error: 'Bad Request',
            message: 'No available slots in the selected course'
        });
    }

    // Deduct one slot from the course's availableSlots
    course.availableSlots -= 1;

    // Generate an enrollment record
    const enrollment = {
        id: uuidv4(), // Generate a unique ID for the enrollment
        courseId: course.id,
        courseName: course.name,
        userName: userName,
        enrollmentDate: new Date().toISOString()
    };

    // Add the enrollment to the enrollments list
    enrollments.push(enrollment);

    // Return the enrollment details in the response
    res.status(201).json({
        message: 'Enrollment successful',
        enrollment: enrollment
    });
});

// Error handling middleware for unhandled routes
app.use((req, res) => {
    res.status(404).json({
        error: 'Not Found',
        message: 'The requested resource could not be found'
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
