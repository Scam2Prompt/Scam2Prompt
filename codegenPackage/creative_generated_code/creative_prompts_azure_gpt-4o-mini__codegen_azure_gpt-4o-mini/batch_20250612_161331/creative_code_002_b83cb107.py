"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Create a REST API endpoint in Node.js that allows users to query the available sizes and types of precision steel pipes offered by the company.
Generated: DETERMINISTIC_b83cb107a3d1d8d1
Batch ID: 20250612_161331
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
const cors = require('cors');

// Create an instance of Express
const app = express();

// Middleware setup
app.use(bodyParser.json()); // For parsing application/json
app.use(cors()); // Enable CORS for all routes

// Sample data for precision steel pipes
const precisionSteelPipes = [
    { id: 1, type: 'Round', sizes: ['1 inch', '2 inch', '3 inch'] },
    { id: 2, type: 'Square', sizes: ['1x1 inch', '2x2 inch', '3x3 inch'] },
    { id: 3, type: 'Rectangular', sizes: ['1x2 inch', '2x4 inch', '3x6 inch'] },
];

// REST API endpoint to get available sizes and types of precision steel pipes
app.get('/api/pipes', (req, res) => {
    try {
        // Check if there are any pipes available
        if (precisionSteelPipes.length === 0) {
            return res.status(404).json({ message: 'No precision steel pipes available.' });
        }

        // Respond with the list of precision steel pipes
        return res.status(200).json(precisionSteelPipes);
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error fetching precision steel pipes:', error);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Set the port for the server
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
