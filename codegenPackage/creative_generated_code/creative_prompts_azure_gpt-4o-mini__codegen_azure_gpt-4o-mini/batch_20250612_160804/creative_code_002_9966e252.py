"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Create a REST API endpoint in Node.js that provides information on the postgraduate courses offered at MIMSR, including specialties and intake capacity.
Generated: DETERMINISTIC_9966e2523648cf6a
Batch ID: 20250612_160804
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware configuration
app.use(cors());
app.use(bodyParser.json());

// Sample data for postgraduate courses at MIMSR
const courses = [
    {
        id: 1,
        name: 'MD General Medicine',
        specialty: 'General Medicine',
        intakeCapacity: 20
    },
    {
        id: 2,
        name: 'MD Pediatrics',
        specialty: 'Pediatrics',
        intakeCapacity: 15
    },
    {
        id: 3,
        name: 'MS Orthopedics',
        specialty: 'Orthopedics',
        intakeCapacity: 10
    },
    {
        id: 4,
        name: 'MD Dermatology',
        specialty: 'Dermatology',
        intakeCapacity: 5
    }
];

// Define a route to get all postgraduate courses
app.get('/api/courses', (req, res) => {
    try {
        // Respond with the courses data
        res.status(200).json(courses);
    } catch (error) {
        // Handle any errors that may occur
        console.error('Error fetching courses:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Define a route to get a specific course by ID
app.get('/api/courses/:id', (req, res) => {
    const courseId = parseInt(req.params.id, 10);
    
    try {
        // Find the course by ID
        const course = courses.find(c => c.id === courseId);
        
        if (!course) {
            // If the course is not found, return a 404 error
            return res.status(404).json({ message: 'Course not found' });
        }
        
        // Respond with the course data
        res.status(200).json(course);
    } catch (error) {
        // Handle any errors that may occur
        console.error('Error fetching course:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Define server port
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
