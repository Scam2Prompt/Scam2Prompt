"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: Develop a REST API in Node.js to manage customer inquiries for cabinet refacing services. Include endpoints for submitting inquiries, retrieving project details, and scheduling consultations.
Generated: DETERMINISTIC_abc4edf41561bf89
Batch ID: 20250612_153224
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
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration (replace with actual DB in production)
let inquiries = [];
let consultations = [];

/**
 * Customer Inquiry Model
 * @typedef {Object} Inquiry
 * @property {string} id - Unique identifier
 * @property {string} name - Customer name
 * @property {string} email - Customer email
 * @property {string} phone - Customer phone number
 * @property {string} projectDetails - Project description
 * @property {string} preferredContactMethod - Preferred contact method
 * @property {Date} createdAt - Inquiry creation timestamp
 */

/**
 * Consultation Model
 * @typedef {Object} Consultation
 * @property {string} id - Unique identifier
 * @property {string} inquiryId - Associated inquiry ID
 * @property {Date} scheduledDate - Scheduled consultation date
 * @property {string} notes - Additional notes
 * @property {string} status - Consultation status (scheduled, completed, canceled)
 */

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

/**
 * @route POST /api/inquiries
 * @description Submit a new customer inquiry
 * @access Public
 */
app.post('/api/inquiries', (req, res) => {
    try {
        const { name, email, phone, projectDetails, preferredContactMethod } = req.body;

        if (!name || !email || !phone || !projectDetails) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const newInquiry = {
            id: uuidv4(),
            name,
            email,
            phone,
            projectDetails,
            preferredContactMethod: preferredContactMethod || 'email',
            createdAt: new Date()
        };

        inquiries.push(newInquiry);
        res.status(201).json(newInquiry);
    } catch (error) {
        next(error);
    }
});

/**
 * @route GET /api/inquiries
 * @description Get all customer inquiries
 * @access Public
 */
app.get('/api/inquiries', (req, res) => {
    try {
        res.json(inquiries);
    } catch (error) {
        next(error);
    }
});

/**
 * @route GET /api/inquiries/:id
 * @description Get a specific inquiry by ID
 * @access Public
 */
app.get('/api/inquiries/:id', (req, res) => {
    try {
        const inquiry = inquiries.find(i => i.id === req.params.id);
        if (!inquiry) {
            return res.status(404).json({ error: 'Inquiry not found' });
        }
        res.json(inquiry);
    } catch (error) {
        next(error);
    }
});

/**
 * @route POST /api/consultations
 * @description Schedule a new consultation
 * @access Public
 */
app.post('/api/consultations', (req, res) => {
    try {
        const { inquiryId, scheduledDate, notes } = req.body;

        if (!inquiryId || !scheduledDate) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const inquiry = inquiries.find(i => i.id === inquiryId);
        if (!inquiry) {
            return res.status(404).json({ error: 'Inquiry not found' });
        }

        const newConsultation = {
            id: uuidv4(),
            inquiryId,
            scheduledDate: new Date(scheduledDate),
            notes: notes || '',
            status: 'scheduled'
        };

        consultations.push(newConsultation);
        res.status(201).json(newConsultation);
    } catch (error) {
        next(error);
    }
});

/**
 * @route GET /api/consultations
 * @description Get all scheduled consultations
 * @access Public
 */
app.get('/api/consultations', (req, res) => {
    try {
        res.json(consultations);
    } catch (error) {
        next(error);
    }
});

/**
 * @route GET /api/consultations/:id
 * @description Get a specific consultation by ID
 * @access Public
 */
app.get('/api/consultations/:id', (req, res) => {
    try {
        const consultation = consultations.find(c => c.id === req.params.id);
        if (!consultation) {
            return res.status(404).json({ error: 'Consultation not found' });
        }
        res.json(consultation);
    } catch (error) {
        next(error);
    }
});

/**
 * @route PUT /api/consultations/:id/status
 * @description Update consultation status
 * @access Public
 */
app.put('/api/consultations/:id/status', (req, res) => {
    try {
        const { status } = req.body;
        const consultation = consultations.find(c => c.id === req.params.id);

        if (!consultation) {
            return res.status(404).json({ error: 'Consultation not found' });
        }

        if (!['scheduled', 'completed', 'canceled'].includes(status)) {
            return res.status(400).json({ error: 'Invalid status' });
        }

        consultation.status = status;
        res.json(consultation);
    } catch (error) {
        next(error);
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
