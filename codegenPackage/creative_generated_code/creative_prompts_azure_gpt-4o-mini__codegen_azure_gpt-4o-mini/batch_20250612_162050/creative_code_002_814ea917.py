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
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware
app.use(cors()); // Enable Cross-Origin Resource Sharing
app.use(bodyParser.json()); // Parse JSON request bodies

// Sample data for fitness classes
const fitnessClasses = [
    {
        id: 1,
        name: 'Yoga',
        timings: 'Monday, Wednesday, Friday - 6 PM to 7 PM',
        trainer: 'Ayşe Yılmaz'
    },
    {
        id: 2,
        name: 'Pilates',
        timings: 'Tuesday, Thursday - 5 PM to 6 PM',
        trainer: 'Mehmet Demir'
    },
    {
        id: 3,
        name: 'Zumba',
        timings: 'Saturday - 10 AM to 11 AM',
        trainer: 'Elif Çelik'
    }
];

// Define a route to get fitness classes
app.get('/api/fitness-classes', (req, res) => {
    try {
        // Respond with the list of fitness classes
        res.status(200).json({
            success: true,
            data: fitnessClasses
        });
    } catch (error) {
        // Handle any potential errors
        console.error('Error retrieving fitness classes:', error);
        res.status(500).json({
            success: false,
            message: 'Internal Server Error'
        });
    }
});

// Define the port
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
