"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Node.js API endpoint to retrieve detailed information about a specific boat, such as "Celebrity 170," including its features like foam flotation and Yamaha outboard motor.
Generated: DETERMINISTIC_b328f4e91a2dec62
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const app = express();
const port = 3000;

// Sample boat data
const boats = {
    'Celebrity 170': {
        name: 'Celebrity 170',
        manufacturer: 'Celebrity Boats',
        year: 2022,
        length: '17 feet',
        capacity: 6,
        features: {
            flotation: 'Foam flotation',
            motor: 'Yamaha 90 HP outboard motor',
            hullMaterial: 'Fiberglass',
            fuelType: 'Gasoline',
            fuelCapacity: '25 gallons'
        },
        price: 28900
    },
    // Add more boats as needed
};

// Middleware to parse JSON requests
app.use(express.json());

/**
 * GET /boats/:boatName
 * Retrieves detailed information about a specific boat
 */
app.get('/boats/:boatName', (req, res) => {
    try {
        const boatName = req.params.boatName;
        const boat = boats[boatName];

        if (!boat) {
            return res.status(404).json({
                error: 'Boat not found',
                message: `No boat found with name: ${boatName}`
            });
        }

        res.json(boat);
    } catch (error) {
        console.error('Error retrieving boat details:', error);
        res.status(500).json({
            error: 'Internal server error',
            message: 'An unexpected error occurred while processing your request'
        });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        error: 'Internal server error',
        message: 'Something went wrong!'
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Boat API server running on port ${port}`);
});

module.exports = app; // For testing purposes
```
