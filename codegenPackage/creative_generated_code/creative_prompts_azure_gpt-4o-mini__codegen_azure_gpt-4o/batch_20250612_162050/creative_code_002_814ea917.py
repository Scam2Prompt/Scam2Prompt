"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Create a REST API endpoint in Node.js that allows users to retrieve information about fitness classes offered at Batıkent Tofaş Spor Klübü, including timings and trainers.
Generated: DETERMINISTIC_814ea917af3c192e
Batch ID: 20250612_162050
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
const express = require('express'); // Framework for building web applications
const bodyParser = require('body-parser'); // Middleware for parsing incoming request bodies

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000; // Port the server will listen on

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Mock fitness classes data
const fitnessClasses = [
  {
    id: 1,
    name: 'Yoga',
    timings: 'Monday, Wednesday, Friday - 6:00 PM to 7:00 PM',
    trainer: 'Alice Johnson',
  },
  {
    id: 2,
    name: 'Pilates',
    timings: 'Tuesday, Thursday - 7:00 PM to 8:00 PM',
    trainer: 'Bob Smith',
  },
  {
    id: 3,
    name: 'Zumba',
    timings: 'Saturday, Sunday - 10:00 AM to 11:00 AM',
    trainer: 'Catherine Lee',
  },
];

// API endpoint to retrieve fitness classes
app.get('/api/fitness-classes', (req, res) => {
  try {
    // Return the list of fitness classes
    res.status(200).json({
      success: true,
      data: fitnessClasses,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error retrieving fitness classes:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching fitness class information.',
    });
  }
});

// Handle undefined routes (404 errors)
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Route not found',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

// Export the app (useful for testing or reusing in other modules)
module.exports = app;
```
