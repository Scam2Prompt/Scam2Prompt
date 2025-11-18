"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Create a REST API endpoint in Node.js for INESO that allows users to fetch details about available courses, including their duration, modality, and accreditation status.
Generated: DETERMINISTIC_b4547efe5eedb565
Batch ID: 20250612_145136
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
const cors = require('cors');

// Create an instance of the Express app
const app = express();

// Middleware configuration
app.use(cors()); // Allow cross-origin requests
app.use(bodyParser.json()); // Parse JSON bodies

// Mock database of courses
const courses = [
    {
        id: 1,
        name: 'Full Stack Development',
        duration: '6 months',
        modality: 'Online',
        accreditation: 'Accredited'
    },
    {
        id: 2,
        name: 'Data Science',
        duration: '4 months',
        modality: 'In-Person',
        accreditation: 'Not Accredited'
    },
    {
        id: 3,
        name: 'Cybersecurity',
        duration: '5 months',
        modality: 'Hybrid',
        accreditation: 'Accredited'
    }
];

// Define a GET endpoint to fetch available courses
app.get('/api/courses', (req, res) => {
    try {
        // Return the list of courses with a success status
        res.status(200).json(courses);
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error fetching courses:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
