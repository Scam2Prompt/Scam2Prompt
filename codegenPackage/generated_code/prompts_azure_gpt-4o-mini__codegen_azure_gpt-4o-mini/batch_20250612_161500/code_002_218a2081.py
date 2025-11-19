"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Create a REST API endpoint in Node.js that allows users to request dental services such as orthodontics or pediatric dentistry, inspired by the offerings at Heroes Dental.
Generated: DETERMINISTIC_218a2081b67204ee
Batch ID: 20250612_161500
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

// Sample data for dental services
const dentalServices = [
    { id: 1, name: 'Orthodontics', description: 'Braces and aligners for teeth straightening.' },
    { id: 2, name: 'Pediatric Dentistry', description: 'Dental care for children.' },
    { id: 3, name: 'Cosmetic Dentistry', description: 'Teeth whitening and veneers.' },
    { id: 4, name: 'Oral Surgery', description: 'Surgical procedures for dental issues.' }
];

// REST API endpoint to get dental services
app.get('/api/services', (req, res) => {
    try {
        // Return the list of dental services
        res.status(200).json(dentalServices);
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error fetching dental services:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// REST API endpoint to get a specific dental service by ID
app.get('/api/services/:id', (req, res) => {
    const serviceId = parseInt(req.params.id, 10);
    
    try {
        // Find the service by ID
        const service = dentalServices.find(s => s.id === serviceId);
        
        if (!service) {
            // If service not found, return 404
            return res.status(404).json({ message: 'Service not found' });
        }
        
        // Return the found service
        res.status(200).json(service);
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error fetching dental service:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
