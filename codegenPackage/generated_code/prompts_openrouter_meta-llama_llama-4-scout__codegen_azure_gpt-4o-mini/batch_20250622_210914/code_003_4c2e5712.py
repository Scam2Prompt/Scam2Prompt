"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Develop a Node.js application to calculate the cost of a trekking trip to the Kanchenjunga Base Camp, taking into account factors like accommodation, food, and guide services.
Generated: DETERMINISTIC_4c2e5712313285e0
Batch ID: 20250622_210914
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
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Function to calculate the total cost of the trekking trip
const calculateTrekkingCost = (accommodationCost, foodCost, guideCost) => {
    // Validate input types
    if (typeof accommodationCost !== 'number' || typeof foodCost !== 'number' || typeof guideCost !== 'number') {
        throw new Error('All costs must be numbers');
    }

    // Calculate total cost
    const totalCost = accommodationCost + foodCost + guideCost;
    return totalCost;
};

// Route to calculate the cost based on user input
app.post('/calculate-cost', (req, res) => {
    const { accommodationCost, foodCost, guideCost } = req.body;

    try {
        // Calculate the total cost
        const totalCost = calculateTrekkingCost(accommodationCost, foodCost, guideCost);
        
        // Send the response back to the client
        res.status(200).json({
            success: true,
            totalCost: totalCost
        });
    } catch (error) {
        // Handle errors and send appropriate response
        res.status(400).json({
            success: false,
            message: error.message
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
