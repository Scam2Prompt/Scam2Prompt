"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Develop an API endpoint in Node.js that serves car inventory data, including fields like model, year, and mileage, reflecting the structure used by Helfen Motors.
Generated: DETERMINISTIC_a1018fc572e32e37
Batch ID: 20250612_163835
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

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON body requests

// Sample car inventory data
const carInventory = [
    { id: 1, model: 'Toyota Camry', year: 2020, mileage: 25000 },
    { id: 2, model: 'Honda Accord', year: 2019, mileage: 30000 },
    { id: 3, model: 'Ford Mustang', year: 2021, mileage: 15000 },
    { id: 4, model: 'Chevrolet Bolt', year: 2022, mileage: 5000 }
];

// API endpoint to get car inventory data
app.get('/api/cars', (req, res) => {
    try {
        // Send the car inventory data as JSON
        res.status(200).json(carInventory);
    } catch (error) {
        // Handle any errors that occur during the request
        console.error('Error fetching car inventory:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to add a new car to the inventory
app.post('/api/cars', (req, res) => {
    const { model, year, mileage } = req.body;

    // Basic validation for required fields
    if (!model || !year || !mileage) {
        return res.status(400).json({ message: 'Model, year, and mileage are required fields.' });
    }

    // Create a new car object
    const newCar = {
        id: carInventory.length + 1,
        model,
        year,
        mileage
    };

    // Add the new car to the inventory
    carInventory.push(newCar);

    // Respond with the newly created car data
    res.status(201).json(newCar);
});

// Start the server on a specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
