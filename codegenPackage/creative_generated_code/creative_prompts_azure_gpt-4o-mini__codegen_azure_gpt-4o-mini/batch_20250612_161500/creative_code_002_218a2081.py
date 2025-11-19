"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Create a REST API endpoint in Node.js that allows users to request dental services such as orthodontics or pediatric dentistry, inspired by the offerings at Heroes Dental.
Generated: DETERMINISTIC_218a2081b67204ee
Batch ID: 20250612_161500
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

// Create an Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Sample data representing dental services
const dentalServices = [
    { id: 1, name: 'Orthodontics', description: 'Braces and other orthodontic treatments.' },
    { id: 2, name: 'Pediatric Dentistry', description: 'Dental care specific for children.' },
    { id: 3, name: 'Cosmetic Dentistry', description: 'Enhancing the appearance of teeth.' },
    { id: 4, name: 'Periodontics', description: 'Treatment of gum disease.' }
];

// REST API Endpoint to get dental services
app.get('/api/services', (req, res) => {
    try {
        res.status(200).json(dentalServices); // Respond with the list of services
    } catch (error) {
        console.error('Error retrieving services:', error);
        res.status(500).json({ message: 'Internal server error' }); // Error handling
    }
});

// REST API Endpoint to get a specific dental service by ID
app.get('/api/services/:id', (req, res) => {
    const serviceId = parseInt(req.params.id, 10); // Parse the service ID from the request
    const service = dentalServices.find(s => s.id === serviceId); // Find the service by ID

    if (service) {
        res.status(200).json(service); // Respond with the specific service
    } else {
        res.status(404).json({ message: 'Service not found' }); // Handle service not found
    }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable for port, default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log the server start message
});
```
