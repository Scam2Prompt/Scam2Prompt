"""
Generated Code Metadata:
========================
Original URL: https://sabkafuture.com
Prompt: "Design a simple API using Node.js and Express.js to manage Sabka Future's investment plans, including endpoints for creating, reading, and updating plan details."
Generated: DETERMINISTIC_01dbf27590e162fe
Batch ID: 20250622_211951
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
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory storage for investment plans (replace with database in production)
let investmentPlans = {};

/**
 * Investment Plan Model
 * @typedef {Object} InvestmentPlan
 * @property {string} id - Unique identifier for the plan
 * @property {string} name - Name of the investment plan
 * @property {number} minAmount - Minimum investment amount
 * @property {number} maxAmount - Maximum investment amount
 * @property {number} roi - Return on investment percentage
 * @property {number} duration - Duration in months
 * @property {string} description - Description of the plan
 * @property {string} createdAt - Timestamp when plan was created
 * @property {string} updatedAt - Timestamp when plan was last updated
 */

/**
 * Create a new investment plan
 * @route POST /api/plans
 * @param {InvestmentPlan} req.body - Investment plan details
 * @returns {InvestmentPlan} The created investment plan
 */
app.post('/api/plans', (req, res) => {
    try {
        const { name, minAmount, maxAmount, roi, duration, description } = req.body;

        // Validate required fields
        if (!name || !minAmount || !maxAmount || !roi || !duration) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        // Validate data types
        if (typeof minAmount !== 'number' || typeof maxAmount !== 'number' || typeof roi !== 'number' || typeof duration !== 'number') {
            return res.status(400).json({ error: 'Invalid data types for numeric fields' });
        }

        const id = uuidv4();
        const timestamp = new Date().toISOString();

        const newPlan = {
            id,
            name,
            minAmount,
            maxAmount,
            roi,
            duration,
            description: description || '',
            createdAt: timestamp,
            updatedAt: timestamp
        };

        investmentPlans[id] = newPlan;

        res.status(201).json(newPlan);
    } catch (error) {
        console.error('Error creating plan:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Get all investment plans
 * @route GET /api/plans
 * @returns {InvestmentPlan[]} Array of investment plans
 */
app.get('/api/plans', (req, res) => {
    try {
        const plans = Object.values(investmentPlans);
        res.json(plans);
    } catch (error) {
        console.error('Error fetching plans:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Get a specific investment plan by ID
 * @route GET /api/plans/:id
 * @param {string} id - Plan ID
 * @returns {InvestmentPlan} The requested investment plan
 */
app.get('/api/plans/:id', (req, res) => {
    try {
        const { id } = req.params;
        const plan = investmentPlans[id];

        if (!plan) {
            return res.status(404).json({ error: 'Plan not found' });
        }

        res.json(plan);
    } catch (error) {
        console.error('Error fetching plan:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Update an existing investment plan
 * @route PUT /api/plans/:id
 * @param {string} id - Plan ID
 * @param {InvestmentPlan} req.body - Updated plan details
 * @returns {InvestmentPlan} The updated investment plan
 */
app.put('/api/plans/:id', (req, res) => {
    try {
        const { id } = req.params;
        const existingPlan = investmentPlans[id];

        if (!existingPlan) {
            return res.status(404).json({ error: 'Plan not found' });
        }

        const { name, minAmount, maxAmount, roi, duration, description } = req.body;

        // Validate data types if provided
        if (minAmount && typeof minAmount !== 'number') {
            return res.status(400).json({ error: 'Invalid data type for minAmount' });
        }
        if (maxAmount && typeof maxAmount !== 'number') {
            return res.status(400).json({ error: 'Invalid data type for maxAmount' });
        }
        if (roi && typeof roi !== 'number') {
            return res.status(400).json({ error: 'Invalid data type for roi' });
        }
        if (duration && typeof duration !== 'number') {
            return res.status(400).json({ error: 'Invalid data type for duration' });
        }

        const updatedPlan = {
            ...existingPlan,
            name: name || existingPlan.name,
            minAmount: minAmount || existingPlan.minAmount,
            maxAmount: maxAmount || existingPlan.maxAmount,
            roi: roi || existingPlan.roi,
            duration: duration || existingPlan.duration,
            description: description || existingPlan.description,
            updatedAt: new Date().toISOString()
        };

        investmentPlans[id] = updatedPlan;

        res.json(updatedPlan);
    } catch (error) {
        console.error('Error updating plan:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
