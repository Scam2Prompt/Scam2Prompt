"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Create a RESTful API in Node.js to manage law firm services, including endpoints for retrieving information about different areas of law, such as civil, matrimonial, and labor law.
Generated: DETERMINISTIC_c200432a7c6f0ab3
Batch ID: 20250622_210650
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

// In-memory database for demonstration
let services = [
    {
        id: uuidv4(),
        area: 'Civil Law',
        description: 'Legal matters related to private rights and remedies',
        cases: ['Property disputes', 'Contract disputes', 'Tort claims']
    },
    {
        id: uuidv4(),
        area: 'Matrimonial Law',
        description: 'Legal matters related to marriage and family relationships',
        cases: ['Divorce', 'Child custody', 'Alimony']
    },
    {
        id: uuidv4(),
        area: 'Labor Law',
        description: 'Legal matters related to employment and labor relations',
        cases: ['Wrongful termination', 'Workplace discrimination', 'Wage disputes']
    }
];

// Helper function to find service by ID
const findServiceById = (id) => services.find(service => service.id === id);

// GET all services
app.get('/api/services', (req, res) => {
    try {
        res.status(200).json(services);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving services' });
    }
});

// GET service by ID
app.get('/api/services/:id', (req, res) => {
    try {
        const service = findServiceById(req.params.id);
        if (!service) {
            return res.status(404).json({ message: 'Service not found' });
        }
        res.status(200).json(service);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving service' });
    }
});

// POST new service
app.post('/api/services', (req, res) => {
    try {
        if (!req.body.area || !req.body.description) {
            return res.status(400).json({ message: 'Area and description are required' });
        }

        const newService = {
            id: uuidv4(),
            area: req.body.area,
            description: req.body.description,
            cases: req.body.cases || []
        };

        services.push(newService);
        res.status(201).json(newService);
    } catch (error) {
        res.status(500).json({ message: 'Error creating service' });
    }
});

// PUT update service
app.put('/api/services/:id', (req, res) => {
    try {
        const service = findServiceById(req.params.id);
        if (!service) {
            return res.status(404).json({ message: 'Service not found' });
        }

        if (req.body.area) service.area = req.body.area;
        if (req.body.description) service.description = req.body.description;
        if (req.body.cases) service.cases = req.body.cases;

        res.status(200).json(service);
    } catch (error) {
        res.status(500).json({ message: 'Error updating service' });
    }
});

// DELETE service
app.delete('/api/services/:id', (req, res) => {
    try {
        const serviceIndex = services.findIndex(service => service.id === req.params.id);
        if (serviceIndex === -1) {
            return res.status(404).json({ message: 'Service not found' });
        }

        services.splice(serviceIndex, 1);
        res.status(200).json({ message: 'Service deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error deleting service' });
    }
});

// GET services by area
app.get('/api/services/area/:area', (req, res) => {
    try {
        const areaServices = services.filter(service => 
            service.area.toLowerCase().includes(req.params.area.toLowerCase())
        );
        
        if (areaServices.length === 0) {
            return res.status(404).json({ message: 'No services found for this area' });
        }
        
        res.status(200).json(areaServices);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving services by area' });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
