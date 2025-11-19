"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakesrus.net
Prompt: Write a REST API endpoint in Node.js that retrieves a list of healthy food options for active lifestyles, similar to the Iron Man Healthy Choices at Pancakes R Us.
Generated: DETERMINISTIC_e406becda832dbee
Batch ID: 20250612_160656
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

// Initialize the Express application
const app = express();

// Middleware to parse incoming request bodies
app.use(bodyParser.json());

// Sample data representing healthy food options
const healthyFoodOptions = [
    { id: 1, name: 'Quinoa Salad', calories: 220, protein: 8, carbs: 39, fats: 4 },
    { id: 2, name: 'Grilled Chicken', calories: 335, protein: 32, carbs: 0, fats: 7 },
    { id: 3, name: 'Avocado Toast', calories: 300, protein: 6, carbs: 28, fats: 18 },
    { id: 4, name: 'Spinach Smoothie', calories: 180, protein: 4, carbs: 32, fats: 2 },
    { id: 5, name: 'Oatmeal with Berries', calories: 250, protein: 9, carbs: 45, fats: 5 },
];

// REST API endpoint to retrieve healthy food options
app.get('/api/healthy-foods', (req, res) => {
    try {
        // Return the list of healthy food options
        res.status(200).json({
            success: true,
            data: healthyFoodOptions,
        });
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error retrieving healthy food options:', error);
        res.status(500).json({
            success: false,
            message: 'Internal Server Error',
        });
    }
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
