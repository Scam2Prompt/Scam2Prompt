"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pneusml.com
Prompt: Construct a RESTful API endpoint in Node.js that provides information on tire sales and alignment services, inspired by the offerings of Pneus ML.
Generated: DETERMINISTIC_958bd00af8aca2e6
Batch ID: 20250612_163224
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

// Initialize the Express application
const app = express();

// Use body-parser middleware to parse JSON requests
app.use(bodyParser.json());

// Sample data to simulate tire sales and alignment services
const tireSales = [
    { id: 1, brand: 'Michelin', model: 'Pilot Sport 4', price: 150 },
    { id: 2, brand: 'Goodyear', model: 'Eagle F1', price: 160 },
    { id: 3, brand: 'Bridgestone', model: 'Potenza RE-71R', price: 170 }
];

const alignmentServices = [
    { id: 1, type: 'Standard Alignment', price: 75 },
    { id: 2, type: 'Premium Alignment', price: 100 }
];

// Endpoint to get all tire sales
app.get('/api/tire-sales', (req, res) => {
    try {
        res.status(200).json(tireSales);
    } catch (error) {
        console.error('Error fetching tire sales:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to get all alignment services
app.get('/api/alignment-services', (req, res) => {
    try {
        res.status(200).json(alignmentServices);
    } catch (error) {
        console.error('Error fetching alignment services:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to get a specific tire sale by ID
app.get('/api/tire-sales/:id', (req, res) => {
    const tireId = parseInt(req.params.id, 10);
    const tire = tireSales.find(t => t.id === tireId);

    if (tire) {
        res.status(200).json(tire);
    } else {
        res.status(404).json({ message: 'Tire not found' });
    }
});

// Endpoint to get a specific alignment service by ID
app.get('/api/alignment-services/:id', (req, res) => {
    const alignmentId = parseInt(req.params.id, 10);
    const service = alignmentServices.find(s => s.id === alignmentId);

    if (service) {
        res.status(200).json(service);
    } else {
        res.status(404).json({ message: 'Alignment service not found' });
    }
});

// Start the server and listen on a specific port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
