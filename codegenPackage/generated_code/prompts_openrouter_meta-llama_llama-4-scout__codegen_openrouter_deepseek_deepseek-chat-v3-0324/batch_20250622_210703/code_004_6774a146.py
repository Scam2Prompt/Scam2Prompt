"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Create a RESTful API in Node.js to handle requests related to tire and wheel services, including listing services, booking appointments, and providing recommendations for tire types.
Generated: DETERMINISTIC_6774a146d4d6392f
Batch ID: 20250622_210703
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
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration purposes
let services = [
    { id: '1', name: 'Tire Rotation', description: 'Rotating tires to ensure even wear', duration: 30, price: 25 },
    { id: '2', name: 'Wheel Alignment', description: 'Adjusting wheel angles to manufacturer specifications', duration: 45, price: 50 },
    { id: '3', name: 'Tire Replacement', description: 'Replacing old tires with new ones', duration: 60, price: 100 }
];

let appointments = [];
let recommendations = [
    { type: 'All-Season', description: 'Good for all weather conditions', bestFor: 'Daily driving' },
    { type: 'Winter', description: 'Designed for snow and ice', bestFor: 'Cold climates' },
    { type: 'Performance', description: 'High-speed and handling', bestFor: 'Sports cars' }
];

// Routes

/**
 * GET /services - List all available services
 */
app.get('/services', (req, res) => {
    try {
        res.status(200).json(services);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve services' });
    }
});

/**
 * POST /appointments - Book a new appointment
 */
app.post('/appointments', (req, res) => {
    try {
        const { serviceId, customerName, date, time } = req.body;
        
        if (!serviceId || !customerName || !date || !time) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const service = services.find(s => s.id === serviceId);
        if (!service) {
            return res.status(404).json({ error: 'Service not found' });
        }

        const newAppointment = {
            id: uuidv4(),
            serviceId,
            serviceName: service.name,
            customerName,
            date,
            time,
            status: 'booked'
        };

        appointments.push(newAppointment);
        res.status(201).json(newAppointment);
    } catch (error) {
        res.status(500).json({ error: 'Failed to book appointment' });
    }
});

/**
 * GET /appointments - List all appointments
 */
app.get('/appointments', (req, res) => {
    try {
        res.status(200).json(appointments);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve appointments' });
    }
});

/**
 * GET /recommendations - Get tire recommendations
 */
app.get('/recommendations', (req, res) => {
    try {
        res.status(200).json(recommendations);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve recommendations' });
    }
});

/**
 * GET /recommendations/:type - Get specific tire recommendation
 */
app.get('/recommendations/:type', (req, res) => {
    try {
        const type = req.params.type;
        const recommendation = recommendations.find(r => r.type.toLowerCase() === type.toLowerCase());
        
        if (!recommendation) {
            return res.status(404).json({ error: 'Recommendation not found' });
        }
        
        res.status(200).json(recommendation);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve recommendation' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
