"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.getaconsulenze.it
Prompt: Construct a RESTful API endpoint in Node.js that allows users to enroll in the Corsi di formazione offered by Geta Consulenze, including error handling for course availability.
Generated: DETERMINISTIC_41768d997afcabeb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Sample data for courses offered by Geta Consulenze
const courses = {
    'course1': { name: 'Course 1', availableSlots: 5 },
    'course2': { name: 'Course 2', availableSlots: 0 }, // No slots available
    'course3': { name: 'Course 3', availableSlots: 2 },
};

// Endpoint to enroll in a course
app.post('/enroll', (req, res) => {
    const { courseId, userName } = req.body;

    // Validate request body
    if (!courseId || !userName) {
        return res.status(400).json({ error: 'Course ID and User Name are required.' });
    }

    // Check if the course exists
    const course = courses[courseId];
    if (!course) {
        return res.status(404).json({ error: 'Course not found.' });
    }

    // Check if there are available slots
    if (course.availableSlots <= 0) {
        return res.status(400).json({ error: 'No available slots in this course.' });
    }

    // Enroll the user (decrement available slots)
    course.availableSlots -= 1;

    // Respond with success message
    return res.status(200).json({
        message: `Successfully enrolled ${userName} in ${course.name}.`,
        remainingSlots: course.availableSlots,
    });
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
