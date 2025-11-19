"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Create a REST API endpoint in Node.js that provides information about the courses and intake capacity for UG and PG students at MIMSR.
Generated: DETERMINISTIC_63b828f97a51ae22
Batch ID: 20250612_162050
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

// Initialize an Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Sample data for courses and intake capacity
const courses = {
    UG: [
        { name: 'Bachelor of Medicine and Bachelor of Surgery (MBBS)', capacity: 150 },
        { name: 'Bachelor of Science in Nursing (B.Sc Nursing)', capacity: 60 }
    ],
    PG: [
        { name: 'Doctor of Medicine (MD)', capacity: 30 },
        { name: 'Master of Surgery (MS)', capacity: 15 }
    ]
};

// Define a REST API endpoint to get courses information
app.get('/api/courses', (req, res) => {
    try {
        // Respond with the courses data
        res.status(200).json({
            success: true,
            data: courses
        });
    } catch (error) {
        // Handle any errors that occur during the request
        console.error('Error fetching courses:', error);
        res.status(500).json({
            success: false,
            message: 'Internal Server Error'
        });
    }
});

// Error handling for undefined routes
app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: 'Not Found'
    });
});

// Start the server on the specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
