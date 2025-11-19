"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Construct a RESTful API endpoint in Node.js that provides information on tire sales and alignment services, inspired by the offerings of Pneus ML.
Generated: DETERMINISTIC_958bd00af8aca2e6
Batch ID: 20250612_163224
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Sample data for tire sales and alignment services
const services = [
    {
        id: 1,
        type: 'Tire Sales',
        description: 'Wide selection of tires for all vehicle types.',
        priceRange: '$50 - $300',
        availableBrands: ['Michelin', 'Goodyear', 'Bridgestone']
    },
    {
        id: 2,
        type: 'Alignment Services',
        description: 'Precision wheel alignment to improve tire life and vehicle handling.',
        priceRange: '$75 - $150',
        duration: '1 hour'
    }
];

// GET endpoint to retrieve all services
app.get('/api/services', (req, res) => {
    try {
        res.status(200).json(services); // Send services as JSON response
    } catch (error) {
        console.error('Error fetching services:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// GET endpoint to retrieve a specific service by ID
app.get('/api/services/:id', (req, res) => {
    const serviceId = parseInt(req.params.id, 10);
    const service = services.find(s => s.id === serviceId);

    if (!service) {
        return res.status(404).json({ message: 'Service not found' });
    }

    res.status(200).json(service); // Send the specific service as JSON response
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
