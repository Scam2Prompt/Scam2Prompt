"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Create a RESTful API using Node.js to handle requests for plumbing services, including drain cleaning, gas line services, and commercial plumbing.
Generated: DETERMINISTIC_5cbb9d1ec86bd302
Batch ID: 20250622_205802
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

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Sample data for plumbing services
let services = [
    { id: 1, type: 'Drain Cleaning', description: 'Clearing clogged drains and pipes.' },
    { id: 2, type: 'Gas Line Services', description: 'Installation and repair of gas lines.' },
    { id: 3, type: 'Commercial Plumbing', description: 'Plumbing services for commercial properties.' }
];

// GET all services
app.get('/api/services', (req, res) => {
    res.status(200).json(services);
});

// GET a specific service by ID
app.get('/api/services/:id', (req, res) => {
    const serviceId = parseInt(req.params.id, 10);
    const service = services.find(s => s.id === serviceId);
    
    if (service) {
        res.status(200).json(service);
    } else {
        res.status(404).json({ error: 'Service not found' });
    }
});

// POST a new service
app.post('/api/services', (req, res) => {
    const { type, description } = req.body;

    if (!type || !description) {
        return res.status(400).json({ error: 'Type and description are required' });
    }

    const newService = {
        id: services.length + 1,
        type,
        description
    };

    services.push(newService);
    res.status(201).json(newService);
});

// PUT to update an existing service
app.put('/api/services/:id', (req, res) => {
    const serviceId = parseInt(req.params.id, 10);
    const service = services.find(s => s.id === serviceId);

    if (!service) {
        return res.status(404).json({ error: 'Service not found' });
    }

    const { type, description } = req.body;
    if (type) service.type = type;
    if (description) service.description = description;

    res.status(200).json(service);
});

// DELETE a service
app.delete('/api/services/:id', (req, res) => {
    const serviceId = parseInt(req.params.id, 10);
    const serviceIndex = services.findIndex(s => s.id === serviceId);

    if (serviceIndex === -1) {
        return res.status(404).json({ error: 'Service not found' });
    }

    services.splice(serviceIndex, 1);
    res.status(204).send(); // No content to send back
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
