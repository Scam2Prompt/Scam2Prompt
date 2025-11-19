"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Create a REST API endpoint in Node.js that provides information on the postgraduate courses offered at MIMSR, including specialties and intake capacity.
Generated: DETERMINISTIC_9966e2523648cf6a
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express for creating the server
const bodyParser = require('body-parser'); // Middleware for parsing JSON
const morgan = require('morgan'); // HTTP request logger

// Initialize the Express app
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(morgan('dev')); // Log HTTP requests to the console

// Mock data for postgraduate courses at MIMSR
const postGraduateCourses = [
  {
    specialty: 'Orthopedics',
    intakeCapacity: 12,
  },
  {
    specialty: 'General Surgery',
    intakeCapacity: 15,
  },
  {
    specialty: 'Obstetrics and Gynecology',
    intakeCapacity: 10,
  },
  {
    specialty: 'Pediatrics',
    intakeCapacity: 8,
  },
  {
    specialty: 'Anesthesiology',
    intakeCapacity: 6,
  },
];

// Route to get information about postgraduate courses
app.get('/api/postgraduate-courses', (req, res) => {
  try {
    // Respond with the list of courses
    res.status(200).json({
      success: true,
      data: postGraduateCourses,
    });
  } catch (error) {
    // Handle any unexpected errors
    console.error('Error fetching postgraduate courses:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching postgraduate courses.',
    });
  }
});

// Route for health check (optional, for monitoring purposes)
app.get('/api/health', (req, res) => {
  res.status(200).json({
    success: true,
    message: 'API is up and running.',
  });
});

// Handle 404 errors for undefined routes
app.use((req, res, next) => {
  res.status(404).json({
    success: false,
    message: 'Route not found.',
  });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Note:
// - This code assumes you have Node.js and Express installed.
// - To install dependencies, run `npm install express body-parser morgan`.
// - Run the server using `node <filename>.js`.
// - Test the API by making GET requests to `/api/postgraduate-courses`.
```
