"""
Generated Code Metadata:
========================
Original URL: https://cbreimapp.com
Prompt: Write JavaScript code to enable functionality for a web application similar to CBRE IM's investment management platform.
Generated: DETERMINISTIC_1670fd886114949f
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// investmentManagementPlatform.js

/**
 * Investment Management Platform
 * 
 * This module provides functionality for managing investments, including creating, reading, updating, and deleting (CRUD) investment opportunities.
 * 
 * @module investmentManagementPlatform
 */

// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const logger = require('./logger');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/investmentManagementPlatform', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => logger.info('Connected to MongoDB'))
    .catch((error) => logger.error('Error connecting to MongoDB:', error));

// Define investment schema
const investmentSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    investmentType: { type: String, enum: ['equity', 'debt'], required: true },
    status: { type: String, enum: ['open', 'closed', 'pending'], required: true },
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
});

// Create investment model
const Investment = mongoose.model('Investment', investmentSchema);

// Create express app
const app = express();
app.use(express.json());

// Get all investments
app.get('/investments', async (req, res) => {
    try {
        const investments = await Investment.find().exec();
        res.json(investments);
    } catch (error) {
        logger.error('Error getting investments:', error);
        res.status(500).json({ message: 'Error getting investments' });
    }
});

// Get investment by ID
app.get('/investments/:id', async (req, res) => {
    try {
        const investment = await Investment.findById(req.params.id).exec();
        if (!investment) {
            res.status(404).json({ message: 'Investment not found' });
        } else {
            res.json(investment);
        }
    } catch (error) {
        logger.error('Error getting investment:', error);
        res.status(500).json({ message: 'Error getting investment' });
    }
});

// Create new investment
app.post('/investments', async (req, res) => {
    try {
        const investment = new Investment(req.body);
        await investment.save();
        res.json(investment);
    } catch (error) {
        logger.error('Error creating investment:', error);
        res.status(500).json({ message: 'Error creating investment' });
    }
});

// Update existing investment
app.put('/investments/:id', async (req, res) => {
    try {
        const investment = await Investment.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!investment) {
            res.status(404).json({ message: 'Investment not found' });
        } else {
            res.json(investment);
        }
    } catch (error) {
        logger.error('Error updating investment:', error);
        res.status(500).json({ message: 'Error updating investment' });
    }
});

// Delete investment
app.delete('/investments/:id', async (req, res) => {
    try {
        await Investment.findByIdAndRemove(req.params.id);
        res.json({ message: 'Investment deleted successfully' });
    } catch (error) {
        logger.error('Error deleting investment:', error);
        res.status(500).json({ message: 'Error deleting investment' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    logger.info(`Server listening on port ${port}`);
});

// logger.js

const winston = require('winston');

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
        new winston.transports.File({ filename: 'combined.log' })
    ]
});

module.exports = logger;
```
