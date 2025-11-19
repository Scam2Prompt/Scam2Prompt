"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Develop a RESTful API endpoint in Node.js that allows users to submit requests for roof repairs, including fields for location, type of damage, and urgency.
Generated: DETERMINISTIC_edce507ac22404b4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const app = express();

// Middleware
app.use(bodyParser.json());

// In-memory storage for repair requests (replace with database in production)
const repairRequests = {};

/**
 * POST /api/repair-requests
 * Submit a new roof repair request
 */
app.post('/api/repair-requests', (req, res) => {
    try {
        const { location, damageType, urgency } = req.body;

        // Validate required fields
        if (!location || !damageType || !urgency) {
            return res.status(400).json({ error: 'Missing required fields: location, damageType, urgency' });
        }

        // Validate urgency level
        const validUrgencies = ['low', 'medium', 'high'];
        if (!validUrgencies.includes(urgency.toLowerCase())) {
            return res.status(400).json({ error: 'Invalid urgency level. Must be one of: low, medium, high' });
        }

        // Create new repair request
        const requestId = uuidv4();
        const newRequest = {
            id: requestId,
            location,
            damageType,
            urgency: urgency.toLowerCase(),
            status: 'pending',
            createdAt: new Date().toISOString()
        };

        repairRequests[requestId] = newRequest;

        res.status(201).json(newRequest);
    } catch (error) {
        console.error('Error submitting repair request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/repair-requests/:id
 * Get a specific repair request by ID
 */
app.get('/api/repair-requests/:id', (req, res) => {
    try {
        const requestId = req.params.id;
        const request = repairRequests[requestId];

        if (!request) {
            return res.status(404).json({ error: 'Repair request not found' });
        }

        res.json(request);
    } catch (error) {
        console.error('Error fetching repair request:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/repair-requests
 * Get all repair requests (with optional filtering)
 */
app.get('/api/repair-requests', (req, res) => {
    try {
        const { urgency, status } = req.query;
        let requests = Object.values(repairRequests);

        // Apply filters if provided
        if (urgency) {
            requests = requests.filter(req => req.urgency === urgency.toLowerCase());
        }
        if (status) {
            requests = requests.filter(req => req.status === status.toLowerCase());
        }

        res.json(requests);
    } catch (error) {
        console.error('Error fetching repair requests:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
